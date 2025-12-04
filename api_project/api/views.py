# api/views.py
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# Existing view for the read-only list endpoint (ListAPIView)
class BookList(generics.ListAPIView):
    """
    API View to list all books using a read-only ListAPIView.
    Endpoint: /api/books/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# NEW ViewSet for full CRUD operations (ModelViewSet)
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that automatically provides 'list', 'create', 'retrieve', 
    'update', and 'destroy' actions for the Book model.
    Endpoints: /api/books_all/, /api/books_all/<pk>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for full CRUD operations. Requires the user to be authenticated.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # NEW PERMISSION: Require the user to be fully authenticated for all operations
    permission_classes = [IsAuthenticated]