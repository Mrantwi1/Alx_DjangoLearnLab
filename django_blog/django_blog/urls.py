# django_blog/urls.py (Main Project URLS)
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Post CRUD
    path('', blog_views.PostListView.as_view(), name='post-list'),
    path('post/new/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', blog_views.register, name='register'),
    path('profile/', blog_views.register, name='profile'), # Simplification for profile
    # Search
    path('search/', blog_views.search, name='search'),
]