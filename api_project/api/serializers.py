from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    It automatically maps the fields from the Book model to 
    API fields and handles conversion to/from JSON.
    """
    class Meta:
        # The model that this serializer is based on
        model = Book
        
        # The fields that should be included in the API output.
        # '__all__' is a shortcut to include every field on the model.
        # Alternatively, you could list them explicitly: fields = ['id', 'title', 'author', 'published_date']
        fields = '__all__'