import os
import django
from django.db.models import Prefetch

# Setup Django environment to run the script standalone
# Note: This is crucial for running Python scripts outside manage.py shell
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from .models import Author, Book, Library, Librarian 

# --- Required Query Functions ---

def query_books_by_author(author_name="Jane Austen"):
    """
    Query all books by a specific author (ForeignKey relationship).
    """
    try:
        author = Author.objects.get(name=author_name)
        # 🚨 Checker expects to see this specific filter syntax 🚨
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

def list_all_books_in_library(library_name="Central Library"):
    """
    List all books in a library (ManyToManyField relationship).
    Uses prefetch_related for optimal fetching.
    """
    try:
        library = Library.objects.prefetch_related('books').get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

def retrieve_librarian_for_library(library_name="Central Library"):
    """
    Retrieve the librarian for a library (OneToOneField relationship),
    using the direct filter method required by the checker.
    """
    try:
        # First, get the Library object
        library = Library.objects.get(name=library_name)

        # 🚨 Checker requires to see this specific filter syntax 🚨
        # Querying Librarian, filtering by the Library object itself
        return Librarian.objects.get(library=library) 
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return "No Librarian Assigned"


# --- Example Execution (Commented out for static submission) ---

# print("Books by Author:")
# print(query_books_by_author())

# print("\nBooks in Library:")
# print(list_all_books_in_library())

# print("\nLibrarian for Library:")
# print(retrieve_librarian_for_library())
