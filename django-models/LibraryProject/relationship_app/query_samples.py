#!/usr/bin/env python3
"""
query_samples.py
- Ensures sample data exists
- Runs 3 example queries:
  1) All books by an author
  2) All books in a library
  3) The librarian for a library

This script can be run directly:
  python relationship_app/query_samples.py
"""

import os, sys

# ensure project root is importable
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# set the correct settings module for your project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def ensure_sample_data():
    author, _ = Author.objects.get_or_create(name="Kwame")
    b1, _ = Book.objects.get_or_create(title="Django Basics", author=author)
    b2, _ = Book.objects.get_or_create(title="Advanced Django", author=author)

    lib, _ = Library.objects.get_or_create(name="Central Library")
    # add books to library (avoid duplicates)
    lib.books.add(b1, b2)

    librarian, _ = Librarian.objects.get_or_create(name="Akosua", library=lib)
    print("Sample data created/ensured.")

def query_all_books_by_author(author_name):
    qs = Book.objects.filter(author__name=author_name)
    print(f"\nBooks by {author_name}:")
    if qs.exists():
        for b in qs:
            print(" -", b.title)
    else:
        print(" No books found for that author.")

def list_all_books_in_library(library_name):
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
        return
    print(f"\nBooks in {library_name}:")
    for b in lib.books.all():
        print(" -", b.title, f"(author: {b.author.name})")

def retrieve_librarian_for_library(library_name):
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found.")
        return
    try:
        print(f"\nLibrarian for {library_name}: {lib.librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library_name}.")

if __name__ == "__main__":
    ensure_sample_data()
    query_all_books_by_author("Kwame")
    list_all_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")

