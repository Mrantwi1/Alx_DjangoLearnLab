from django.urls import path
from .views import book_list, LibraryDetailView, register # Ensure 'register' is imported

# Import built-in auth views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Existing App Views
    path('books/', book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # --- Authentication Views ---

    # Registration (Custom View)
    path('register/', register, name='register'),

    # Login (Built-in View)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout (Built-in View)
    # The next_page='login' redirects to the login page after successful logout.
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'),
]
