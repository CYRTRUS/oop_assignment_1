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


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []  # List of book IDs

    def can_borrow(self):
        """Check if member can borrow more books"""
        return len(self.borrowed_books) < 3

    def borrow_book(self, book_id):
        """Add a book to member's borrowed list"""
        if self.can_borrow() and book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        """Remove a book from member's borrowed list"""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def get_borrowed_count(self):
        """Get number of books currently borrowed"""
        return len(self.borrowed_books)

    def __str__(self):
        return f"Member {self.id}: {self.name} ({self.email}) - {len(self.borrowed_books)} books borrowed"

# Test the Member class


def test_member_class():
    print("\n=== Testing Member Class ===")

    # Create a member
    member1 = Member(101, "Alice Smith", "alice@email.com")
    print(f"Created: {member1}")

    # Test borrowing
    print("\n--- Testing Book Borrowing ---")
    print(f"Can borrow: {member1.can_borrow()}")

    # Borrow books
    member1.borrow_book(1)
    print(f"After borrowing book 1: {member1}")

    member1.borrow_book(2)
    print(f"After borrowing book 2: {member1}")

    member1.borrow_book(3)
    print(f"After borrowing book 3: {member1}")

    # Try to borrow fourth book
    can_borrow = member1.can_borrow()
    print(f"Can borrow fourth book: {can_borrow}")

    # Test returning
    print("\n--- Testing Book Returning ---")
    member1.return_book(2)
    print(f"After returning book 2: {member1}")

    # Can borrow again after return
    print(f"Can borrow now: {member1.can_borrow()}")


if __name__ == "__main__":
    test_book_class()
    test_member_class()
