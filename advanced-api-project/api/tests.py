from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")
        # Create a book
        self.book = Book.objects.create(
            title="Harry Potter", 
            publication_year=1997, 
            author=self.author
        )
        self.list_url = reverse('book-list')

    def test_get_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        """Test creating a book while logged in"""
        self.client.login(username='testuser', password='password123')
        data = {"title": "The Hobbit", "publication_year": 1937, "author": self.author.id}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books"""
        data = {"title": "Forbidden Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url, {'title': 'Harry Potter'})
        self.assertEqual(len(response.data), 1)