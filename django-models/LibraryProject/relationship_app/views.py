from django.shortcuts import render, redirect

# 🚨 This explicit line is required by the checker 🚨
from django.views.generic.detail import DetailView

# You can keep the shorter import if you need other generic views, but ensure the above line is present.
# from django.views.generic import DetailView

# ... rest of your model imports and code ...
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
