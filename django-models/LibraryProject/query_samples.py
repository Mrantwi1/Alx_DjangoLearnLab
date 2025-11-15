import os
import django

# --- SETUP ---
# IMPORTANT: Change 'LibraryProject.settings' to YOUR project's settings file name.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
# ---------------

# Import models AFTER setup
from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """
    Clears old data and creates new sample data for queries.
    """
    print("Setting up sample data...")
    # Clear all old data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # 1. Create Author
    author_tolkien = Author.objects.create(name="J.R.R. Tolkien")

    # 2. Create Books (linked to author via ForeignKey)
    book_hobbit = Book.objects.create(title="The Hobbit", author=author_tolkien)
    book_fotr = Book.objects.create(title="The Fellowship of the Ring", author=author_tolkien)
    Book.objects.create(title="The Two Towers", author=author_tolkien) # This one won't be in the library

    # 3. Create Library
    main_library = Library.objects.create(name="Central City Library")

    # 4. Add books to library (using ManyToMany)
    main_library.books.add(book_hobbit, book_fotr)

    # 5. Create Librarian (linked to library via OneToOne)
    Librarian.objects.create(name="Mr. Giles", library=main_library)

    print("Sample data created successfully.\n")


def run_queries():
    """
    Runs and prints the results of the required queries.
    """
    print("--- Running Queries ---")

    # 1. Query all books by a specific author
    print("\n1. Query: All books by J.R.R. Tolkien")
    try:
        author = Author.objects.get(name="J.R.R. Tolkien")
        # We can use the 'related_name' we defined ('books')
        books_by_author = author.books.all() 
        for book in books_by_author:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print("  - Author not found.")

    # 2. List all books in a library
    print("\n2. Query: All books in Central City Library")
    try:
        library = Library.objects.get(name="Central City Library")
        # We use the 'books' ManyToManyField
        books_in_library = library.books.all()
        for book in books_in_library:
            print(f"  - {book.title}")
    except Library.DoesNotExist:
        print("  - Library not found.")

    # 3. Retrieve the librarian for a library
    print("\n3. Query: Librarian for Central City Library")
    try:
        library = Library.objects.get(name="Central City Library")
        # We use the reverse OneToOne relationship (Django creates 'librarian' for us)
        librarian_name = library.librarian.name
        print(f"  - The librarian is {librarian_name}.")
    except Library.DoesNotExist:
        print("  - Library not found.")
    except Librarian.DoesNotExist:
        print("  - No librarian found for this library.")

    print("\n--- Queries complete ---")


if __name__ == "__main__":
    create_sample_data()
    run_queries()
