from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Unit tests for the Book API endpoints.
    Covers CRUD, Permissions, Filtering, and Searching.
    """

    def setUp(self):
        # 1. Create a user for authentication
        self.user = User.objects.create_user(username='tester', password='password123')
        
        # 2. Setup initial data
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )
        
        # 3. Define URLs using the 'name' attributes from urls.py
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # --- CRUD TESTS ---

    def test_create_book(self):
        """Verify that an authenticated user can create a book."""
        self.client.login(username='tester', password='password123')
        data = {"title": "Animal Farm", "publication_year": 1945, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Verify that an authenticated user can update a book."""
        self.client.login(username='tester', password='password123')
        data = {"title": "1984 - Special Edition", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "1984 - Special Edition")

    def test_delete_book(self):
        """Verify that an authenticated user can delete a book."""
        self.client.login(username='tester', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- PERMISSION TESTS ---

    def test_create_book_unauthenticated(self):
        """Verify that anonymous users cannot create books (HTTP 403)."""
        data = {"title": "Secret Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- FILTERING & SEARCHING TESTS ---

    def test_filter_by_year(self):
        """Verify filtering by publication_year."""
        response = self.client.get(self.list_url, {'publication_year': 1949})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    def test_search_by_title(self):
        """Verify search functionality."""
        response = self.client.get(self.list_url, {'search': '1984'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")