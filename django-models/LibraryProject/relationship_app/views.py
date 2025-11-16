from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library, Author

# --- 1. Function-based View (FBV) ---
def book_list(request):
    """
    Lists all books using a function-based view.
    """
    # Query all Book objects, ordered by title
    all_books = Book.objects.all().order_by('title')

    # Context dictionary to pass data to the template
    context = {
        'books': all_books
    }

    # Render the list_books.html template
    return render(request, 'relationship_app/list_books.html', context)

# --- 2. Class-based View (CBV) ---
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library using a class-based DetailView.
    """
    # Specifies the model the view will operate on
    model = Library

    # Specifies the name of the template to be rendered
    template_name = 'relationship_app/library_detail.html'

    # Specifies the name of the variable to use in the template (default is 'library')
    context_object_name = 'library'
