from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Post.objects.all()
        # Search functionality using title__icontains
        author_name = self.request.query_params.get('author')
        title_query = self.request.query_params.get('title')
        content_query = self.request.query_params.get('content')
        
        if author_name:
            queryset = queryset.filter(author__username__icontains=author_name)
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        if content_query:
            queryset = queryset.filter(content__icontains=content_query)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Access following users and filter posts
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
