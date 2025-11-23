# ...existing code...
from django.db import models

class Book(models.Model):
    """
    A simple model representing a book, to be used as the data source for the first API endpoint.
    """

    title = models.CharField(max_length=200, help_text="The title of the book.")
    author = models.CharField(max_length=100, help_text="The author of the book.")
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = "Book"

    def __str__(self):
        return f"{self.title} by {self.author}"
# ...existing code...