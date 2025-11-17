from django.db import models
from django.contrib.auth.models import User # Required for UserProfile

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# Library model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)

    def __str__(self):
        return self.name

# Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # Corrected: Ensures 'librarian' is complete and the line is not cut off.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} ({self.library.name})"

# UserProfile model (for Role-Based Access Control)
class UserProfile(models.Model):
    """
    Extends the default User model to include role-based access.
    """
    # Define role choices
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')

    # Role field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
