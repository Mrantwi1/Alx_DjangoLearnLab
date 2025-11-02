from bookshelf.models import Book
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
from bookshelf.models import Book
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
# Output:
# 1984 George Orwell 1949
from bookshelf.models import Book
book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
from bookshelf.models import Book
book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
Book.objects.all()
# Output: <QuerySet []>
