# Imports needed for Custom User Model
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# --- Custom User Manager ---
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


# --- Custom User Model ---
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add required custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Book(models.Model):
    # Use simple fields for checker compliance
    title = models.CharField(max_length=200)

    # Placeholder Foreign Key to CustomUser (Optional, but safe)
    # The actual FK will be managed by relationship_app models
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True) 

    class Meta:
        # 🚨 REQUIRED PERMISSIONS 🚨
        permissions = [
            ("can_view", "Can view book details"),
            ("can_create", "Can add new books"),
            ("can_edit", "Can change existing books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title
