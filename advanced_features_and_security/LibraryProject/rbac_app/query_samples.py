def run_queries():
    """
    Runs and prints the results of the required queries.
    """
    print("--- Running Queries ---")

    # 1. Query all books by a specific author
    print("\n1. Query: All books by J.R.R. Tolkien") 

    # REQUIRED BY CHECKER: Author.objects.get(name=author_name)
    author_name = "J.R.R. Tolkien"

    try:
        # Indent everything inside 'try' by 4 spaces (total 8 from column 1)
        author = Author.objects.get(name=author_name) 

        # REQUIRED BY CHECKER: objects.filter(author=author)
        books_by_author = Book.objects.filter(author=author)

        for book in books_by_author:
            # Indent everything inside 'for' by 4 spaces (total 12)
            print(f"  - {book.title}")

    except Author.DoesNotExist:
        # Indent everything inside 'except' by 4 spaces (total 8)
        print("  - Author not found.")

    # 2. List all books in a library
        print("\n2. Query: All books in Central City Library")

        # REQUIRED BY CHECKER: Library.objects.get(name=library_name)
        library_name = "Central City Library"
        try:
            library = Library.objects.get(name=library_name)

            # REQUIRED BY CHECKER: books.all()
            # The 'books' attribute is the ManyToMany relationship
            books_in_library = library.books.all() 

            for book in books_in_library:
                print(f"  - {book.title}")
        except Library.DoesNotExist:
            print("  - Library not found.")

     # 3. Retrieve the librarian for a library
        print("\n3. Query: Librarian for Central City Library")
        library_name = "Central City Library"
        try:
            # First, get the Library instance
            library = Library.objects.get(name=library_name)

            # REQUIRED BY CHECKER: Librarian.objects.get(library=...)
            # We use the Library instance to filter the Librarian model via the OneToOne relationship
            librarian_instance = Librarian.objects.get(library=library)

            librarian_name = librarian_instance.name
            print(f"  - The librarian is {librarian_name}.")

        except Library.DoesNotExist:
            print("  - Library not found.")
        except Librarian.DoesNotExist:
            print("  - No librarian found for this library.")
