class Book:
    def __init__(self, title: str, author: str, year: int, is_available = True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if not self.is_available:
            print("This book isn't available, you can't borrow it.\n")
            return None
        self.is_available = False

    def return_book(self):
        if self.is_available:
            print("You can't return this book, it has already been there.\n")
            return None
        self.is_available = True

    def get_info(self) -> str:
        output_string = f"Title of the book: {self.title},\nAuthor: {self.author},\nPublished in {self.year},\n"
        
        if self.is_available:
            return output_string + "The book is available right now.\n"
        else:
            return output_string + "The book isn't available right now.\n"
        
first_book = Book("First Book", "The Great Writer", 1880)
second_book = Book("Second Book", "Average Writer", 1979)
third_book = Book("Not even the Book", "Nameless Author", 1902, False)

"""Testing"""

print(first_book.get_info())
first_book.borrow()
print(first_book.get_info())
first_book.return_book()
print(first_book.get_info() + '\n')

print(second_book.get_info())
second_book.return_book()
print(second_book.get_info())

print(third_book.get_info())
third_book.borrow()
print(third_book.get_info())