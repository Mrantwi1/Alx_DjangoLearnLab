from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    This class automatically provides standard RESTful endpoints:
    GET (list, retrieve), POST (create), PUT/PATCH (update), DELETE (destroy).
    """
    # 1. queryset: Defines the data source (all Book objects)
    queryset = Book.objects.all()
    
    # 2. serializer_class: Specifies which serializer to use for data formatting
    serializer_class = BookSerializer