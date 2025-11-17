from django.urls import path
from .views import LibraryDetailView # Import the class directly
from . import views # Ensure this line is present to import the views module

urlpatterns = [
    # ... existing paths (admin-dashboard/, librarian-portal/, member-area/) ...

    urlpatterns = [
    # ... your existing paths ...

    path('add_book/', add_book, name='add_book'), # Changed from views.add_book
    path('edit_book/<int:pk>/', change_book, name='change_book'), # Changed from views.change_book
    path('delete_book/<int:pk>/', delete_book, name='delete_book'), # Changed from views.delete_book

    # This path must use the view name the checker requires
    path('books/', list_books, name='book_list'), # 🚨 MUST use list_books 🚨

    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
