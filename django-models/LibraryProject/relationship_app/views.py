from django.views.generic.detail import DetailView # 👈 Fix for the last error

# 🚨 This line must be present for the current error 🚨
from .models import Library 

# Ensure you still import other necessary models for your views
from .models import Book, Author 

# ... rest of the code ...
def list_book#(request):
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
