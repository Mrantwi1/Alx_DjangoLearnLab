# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# This view is named BookList and extends ListAPIView, as required.
class BookList(generics.ListAPIView):
    """
    API View to list all books using a read-only ListAPIView.
    Endpoint: /api/books/
    """
    # The set of objects to work with
    queryset = Book.objects.all()
    # The serializer used for data conversion
    serializer_class = BookSerializer