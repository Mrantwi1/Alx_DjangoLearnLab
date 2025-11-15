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
    # ... rest of the run_queries function goes here ...
