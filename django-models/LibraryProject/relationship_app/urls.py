from django.urls import path

# 🚨 REQUIRED CHANGE 1: Import the entire views module 🚨
from . import views 

# Import built-in auth views for reference
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    # Existing App Views (use dot notation now if necessary, or keep old imports if they work)
    path('books/', views.list_books, name='book_list'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # 🚨 REQUIRED CHANGE 2: Use views.register 🚨
    path('register/', views.register, name='register'),

    # Authentication Views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'),
]
