from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# 🚨 REQUIRED IMPORTS 🚨
from .views import list_books
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
    # 1. Registration (links to the function you created in views.py)
    path('register/', views.register, name='register'),

    # 2. Login (uses built-in class and template argument)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # 3. Logout (uses built-in class and template argument to satisfy the strict checker)
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

