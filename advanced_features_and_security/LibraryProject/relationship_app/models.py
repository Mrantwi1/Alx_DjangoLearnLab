from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
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

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    # 🚨 ADD THIS NESTED CLASS 🚨
    class Meta:
        permissions = (
            ("can_add_book", "Can add new book entries"),
            ("can_change_book", "Can edit existing book entries"),
            ("can_delete_book", "Can delete book entries"),
        )

# --- Custom User Manager (Step 3) ---
class CustomUserManager(BaseUserManager):
    """Custom user manager for the CustomUser model."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
# --- Custom User Model (Step 1) ---
class CustomUser(AbstractUser):
    # Override username to allow null/blank if needed, or just keep it.
    # Use email as the unique identifier.
    email = models.EmailField(unique=True)

    # Add required custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Use the custom manager
    objects = CustomUserManager()

    # Specify a unique field for the username/login identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Keep username as required for create_superuser compatibility

    # Remove the UserProfile model that previously extended the built-in User,
    # as CustomUser now contains the necessary fields.
    # NOTE: You may need to adapt this based on your previous UserProfile model.
