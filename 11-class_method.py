# Creating a class called Book
class Book:
    # Class variable to keep track of total books
    total_books = 0

    # Constructor to initialize book title
    def __init__(self, title):
        self.title = title
        # Increment total books when a new book is created
        Book.increment_book_count()

    # Class method to increment total_books
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    # Method to display book details
    def display(self):
        print(f"Book Title: {self.title}")

# Creating objects of the Book class
book1 = Book("Harry Potter and the Sorcerer's Stone")
book2 = Book("The Hobbit")

# Displaying the total number of books
print(f"Total books: {Book.total_books}")
