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


class Library:
    def __init__(self):
        self.books = {}  # {book_id: Book object}
        self.members = {}  # {member_id: Member object}
        self.borrowed_books = []  # List of transactions

    def add_book(self, book_id, title, author, total_copies):
        """Add a new book to the library"""
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author, total_copies)
            print(f"Book '{title}' added successfully!")
            return True
        else:
            print("Error: Book ID already exists!")
            return False

    def add_member(self, member_id, name, email):
        """Register a new library member"""
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name, email)
            print(f"Member '{name}' registered successfully!")
            return True
        else:
            print("Error: Member ID already exists!")
            return False

    def find_book(self, book_id):
        """Find a book by ID"""
        return self.books.get(book_id)

    def find_member(self, member_id):
        """Find a member by ID"""
        return self.members.get(member_id)

    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False

        if not book:
            print("Error: Book not found!")
            return False

        if not book.is_available():
            print("Error: No copies available!")
            return False

        if not member.can_borrow():
            print("Error: Member has reached borrowing limit!")
            return False

        # Process the borrowing
        if book.borrow_book() and member.borrow_book(book_id):
            transaction = {
                'member_id': member_id,
                'book_id': book_id,
                'member_name': member.name,
                'book_title': book.title
            }
            self.borrowed_books.append(transaction)
            print(f"{member.name} borrowed '{book.title}'")
            return True

        return False

    def return_book(self, member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        # Process the return
        if book.return_book() and member.return_book(book_id):
            # Remove from borrowed_books list
            for i, transaction in enumerate(self.borrowed_books):
                if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                    self.borrowed_books.pop(i)
                    break
            print(f"{member.name} returned '{book.title}'")
            return True

        return False

    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        available_found = False
        for book in self.books.values():
            if book.is_available():
                print(f"- {book}")
                available_found = True
        if not available_found:
            print("No books available at the moment.")

    def display_member_books(self, member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")

# Test the Library class


def test_library_class():
    print("\n=== Testing Library Class ===")

    library = Library()

    # Add books
    print("\n--- Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)

    # Add members
    print("\n--- Adding Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")

    # Display available books
    print("\n--- Available Books ---")
    library.display_available_books()

    # Test borrowing
    print("\n--- Testing Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python

    # Display member books
    print("\n--- Member's Books ---")
    library.display_member_books(101)
    library.display_member_books(102)

    # Display available books after borrowing
    print("\n--- Available Books After Borrowing ---")
    library.display_available_books()

    # Test returning
    print("\n--- Testing Returning ---")
    library.return_book(101, 1)
    library.display_member_books(101)
    library.display_available_books()


def test_complete_system():
    """Comprehensive test of the complete OOP system"""
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - OOP COMPREHENSIVE TEST")
    print("=" * 60)

    library = Library()

    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    library.add_book(2, "Clean Code", "Robert Martin", 2)
    library.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    library.add_book(4, "Design Patterns", "Gang of Four", 2)

    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(101, "Alice Smith", "alice@email.com")
    library.add_member(102, "Bob Jones", "bob@email.com")
    library.add_member(103, "Carol White", "carol@email.com")

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)  # Alice borrows Python Crash Course
    library.borrow_book(101, 2)  # Alice borrows Clean Code
    library.borrow_book(102, 1)  # Bob borrows Python Crash Course

    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)  # Alice's books
    library.display_member_books(102)  # Bob's books
    library.display_member_books(103)  # Carol's books (none)

    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    # Carol borrows the only copy of Pragmatic Programmer
    library.borrow_book(103, 3)
    library.display_available_books()

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)  # Bob tries to borrow unavailable book

    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)  # Alice's 3rd book
    library.display_member_books(101)
    library.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)  # Alice returns Python Crash Course
    library.return_book(102, 1)  # Bob returns Python Crash Course
    library.display_member_books(101)
    library.display_available_books()

    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)  # Bob tries to return book he didn't borrow

    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)  # Carol returns Pragmatic Programmer
    library.borrow_book(102, 3)  # Bob borrows it
    library.display_member_books(102)

    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)  # Non-existent member
    library.borrow_book(101, 999)  # Non-existent book
    library.return_book(999, 1)  # Non-existent member
    library.display_member_books(999)  # Non-existent member

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in library.borrowed_books:
        print(
            f"  {transaction['member_name']} has '{transaction['book_title']}'")

    print("\nAll Members and Their Books:")
    for member in library.members.values():
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books:
            for book_id in member.borrowed_books:
                book = library.find_book(book_id)
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")

    library.display_available_books()

    print("\n" + "=" * 60)
    print("OOP TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
    test_member_class()
    test_library_class()

    # Run comprehensive integration test
    test_complete_system()
