from django.db import models

class Author(models.Model):
    """
    Stores an author's name.
    One author can have many books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Stores book details and links to an Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # ForeignKey creates a one-to-many relationship
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title