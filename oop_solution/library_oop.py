class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        """Borrow one copy of this book"""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        """Return one copy of this book"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def is_available(self):
        """Check if book is available"""
        return self.available_copies > 0

    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.available_copies}/{self.total_copies} available"

# Test the Book class


def test_book_class():
    print("=== Testing Book Class ===")

    # Create a book
    book1 = Book(1, "Python Crash Course", "Eric Matthes", 3)
    print(f"Created: {book1}")

    # Test borrowing
    print("\n--- Testing Borrowing ---")
    success1 = book1.borrow_book()
    print(f"First borrow: {success1} - {book1}")

    success2 = book1.borrow_book()
    print(f"Second borrow: {success2} - {book1}")

    success3 = book1.borrow_book()
    print(f"Third borrow: {success3} - {book1}")

    success4 = book1.borrow_book()  # Should fail
    print(f"Fourth borrow: {success4} - {book1}")

    # Test returning
    print("\n--- Testing Returning ---")
    book1.return_book()
    print(f"After return: {book1}")

    book1.return_book()
    print(f"After second return: {book1}")


if __name__ == "__main__":
    test_book_class()
