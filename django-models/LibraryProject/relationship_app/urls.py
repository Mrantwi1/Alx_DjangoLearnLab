from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    # FBV: /relationship/books/
    path('books/', book_list, name='book_list'),

    # CBV: /relationship/library/<pk>/
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
