from django.urls import path

# 🚨 REQUIRED IMPORTS 🚨
from .views import add_book, change_book, delete_book, list_books, LibraryDetailView

urlpatterns = [
    # RBAC Views
    path('admin-dashboard/', list_books, name='admin_view'),
    path('librarian-portal/', list_books, name='librarian_view'),
    path('member-area/', list_books, name='member_view'),

    # Custom Permissions (CRUD) Views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', change_book, name='change_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

    # Function-based View (Required for list_books)
    path('books/', list_books, name='book_list'),

    # Class-based View (Required for library_detail)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
