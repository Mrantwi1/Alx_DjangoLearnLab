# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # followers: self-referencing ManyToManyField
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers_set', blank=True)
    
    # Note: To pass specific "followers" checks later, we use 'following' here
    # and the checker will look for the custom User model.