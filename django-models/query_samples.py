import os
import django

# Set up the Django environment
# NOTE: This block is usually needed if the script is run outside manage.py shell
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.models import User
from django.db.models import Count, Max

# --- Query Samples ---

def get_author_by_name(name):
    """Retrieves a single Author object by name."""
    try:
        return Author.objects.get(name=name)
    except Author.DoesNotExist:
        return None

def get_books_by_author(author_name):
    """Retrieves all books written by a specific author (ForeignKey reverse lookup)."""
    return Book.objects.filter(author__name=author_name)

def get_library_with_book_count():
    """Retrieves all libraries and annotates them with the number of books they hold (M2M aggregation)."""
    return Library.objects.annotate(book_count=Count('books')).order_by('-book_count')

def get_librarian_library(librarian_name):
    """Retrieves the Library associated with a specific Librarian (OneToOne forward lookup)."""
    try:
        # Assuming Librarian model has a name field
        librarian = Librarian.objects.get(name=librarian_name)
        return librarian.library
    except Librarian.DoesNotExist:
        return None

def get_user_role(username):
    """Retrieves the role of a user using the UserProfile (OneToOne reverse lookup)."""
    try:
        user = User.objects.get(username=username)
        # Accesses the UserProfile through the related_name 'userprofile'
        return user.userprofile.role
    except User.DoesNotExist:
        return None
    except UserProfile.DoesNotExist:
        return "Profile Not Found"

# --- Example Usage (Commented out for static submission) ---

# print("\n--- Queries ---")
# # Assuming a user named 'admin_user' exists
# print(f"User Role: {get_user_role('admin_user')}") 
# # Assuming an author named 'Jane Austen' exists
# print(f"Books by Author: {get_books_by_author('Jane Austen')}")
# # Print libraries by book count
# print("Libraries by book count:")
# for lib in get_library_with_book_count():
#     print(f"  {lib.name}: {lib.book_count} books")
