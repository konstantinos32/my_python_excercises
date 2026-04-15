
#1
class Book:
    def __init__(self, name, author, release_year):
        self.name = name
        self.author = author
        self.release_year = release_year
        self.book_read = False

my_book = Book("Bio", "kostas", 2020)
my_book2 = Book("Bio", "kosta", 2020)


print(my_book.name)

#2

class BookCollection:
    def __init__(self,books=None):
        if books is None:
            self.books = []
        else:
            for book in books:
                if not isinstance(book,Book):
                    raise Exception("All items must be instances of the Book class.")
            self.books = books

#3
    def add_book(self,book):
        if not isinstance(book,Book):
            raise Exception("The item is not an instance of the Book class.")
        self.books.append(book)
#4
    def mark_as_read(self,book_name):
        for book in self.books:
            if book.name ==book.name:
                book.book_read = True
                return
        print(f"Book with name '{book_name}' not found in the collection.")

        

#5
    def list_books(self):
        for book in self.books:
            status = "Read" if book.book_read else "Not Read"
            print(f"{book.name} by {book.author} ({book.release_year}) - {status}")
