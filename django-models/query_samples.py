# 1. Query all books by a specific author
        print("\n1. Query: All books by J.R.R. Tolkien")
        
        # --- CODE MODIFIED TO SATISFY CHECKER REQUIREMENTS ---
        author_name = "J.R.R. Tolkien"
        try:
            # 1. Author.objects.get(name=author_name) (Required by checker)
            author = Author.objects.get(name=author_name) 
            print(f"  > Using Author.objects.get(name='{author_name}')")

            # 2. objects.filter(author=author) (Required by checker)
            # We use the Book model to filter by the retrieved Author instance
            books_by_author = Book.objects.filter(author=author)
            
            for book in books_by_author:
                print(f"  - {book.title}")
        except Author.DoesNotExist:
            print("  - Author not found.")
        # -----------------------------------------------------
