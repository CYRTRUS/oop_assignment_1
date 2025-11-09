# Library Management System - Object-Oriented Design

## Project Overview

This project is a comprehensive Library Management System refactored from procedural code to an object-oriented design. The system manages book inventory, member registrations, borrowing operations, and return processes. It provides a robust foundation for library operations with proper error handling and validation.

## Project Structure

```bash
oop_assignment_1/
├── README.md                    # This file
├── procedural_version/
│   ├── library_procedural.py    # Original procedural code
│   └── test_procedural.py       # Comprehensive test suite
└── oop_solution/
    ├── library_oop.py           # Student's OOP implementation (to create)
    └── test_oop.py              # Tests for OOP version (to create)
```

## Design Overview

### Book Class

**Purpose**: Represents individual books in the library inventory.

**Attributes**:

- `id` (int): Unique identifier for the book
- `title` (str): Title of the book
- `author` (str): Author of the book
- `total_copies` (int): Total number of copies owned by the library
- `available_copies` (int): Number of copies currently available for borrowing

**Key Methods**:

- `borrow_book()`: Decrements available copies when borrowed
- `return_book()`: Increments available copies when returned
- `is_available()`: Checks if any copies are available
- `__str__()`: Provides formatted string representation

### Member Class

**Purpose**: Represents library members who can borrow books.

**Attributes**:

- `id` (int): Unique identifier for the member
- `name` (str): Full name of the member
- `email` (str): Contact email address
- `borrowed_books` (list): List of book IDs currently borrowed

**Key Methods**:

- `can_borrow()`: Checks if member can borrow more books (limit: 3)
- `borrow_book(book_id)`: Adds book to borrowed list
- `return_book(book_id)`: Removes book from borrowed list
- `get_borrowed_count()`: Returns number of books currently borrowed
- `__str__()`: Provides formatted string representation

### Library Class

**Purpose**: Manages the entire library system, coordinating books and members.

**Attributes**:

- `books` (dict): Dictionary mapping book_id to Book objects
- `members` (dict): Dictionary mapping member_id to Member objects
- `borrowed_books` (list): List of active borrowing transactions

**Key Methods**:

- `add_book()`: Adds new book to library collection
- `add_member()`: Registers new library member
- `find_book()`: Retrieves book by ID
- `find_member()`: Retrieves member by ID
- `borrow_book()`: Processes book borrowing with validation
- `return_book()`: Processes book returns with validation
- `display_available_books()`: Shows all available books
- `display_member_books()`: Shows books borrowed by specific member

## Testing

The system includes comprehensive test coverage through `test_complete_system()` function that validates:

### Basic Operations

- ✅ Adding books to library inventory
- ✅ Registering new library members
- ✅ Successful book borrowing transactions
- ✅ Successful book return transactions
- ✅ Displaying available books
- ✅ Displaying member's borrowed books

### Edge Cases

- ✅ **Borrowing unavailable books**: Prevents borrowing when no copies available
- ✅ **Exceeding borrowing limit**: Enforces 3-book maximum per member
- ✅ **Returning books not borrowed**: Validates member actually borrowed the book
- ✅ **Non-existent books/members**: Handles invalid IDs gracefully
- ✅ **Duplicate book/member IDs**: Prevents adding duplicates
- ✅ **Borrowing last available copy**: Updates availability correctly

### Test Scenarios Covered

1. **Inventory Management**: Adding books and members
2. **Borrowing Workflow**: Successful borrow operations
3. **Availability Tracking**: Real-time copy availability updates
4. **Member Limits**: Enforcement of 3-book borrowing limit
5. **Return Processing**: Proper handling of book returns
6. **Error Handling**: Comprehensive validation and error messages
7. **System Integration**: End-to-end workflow testing

## How to Run the Test Code

### Running the Tests

1. **Clone or download the project files**
   ```bash
   cd oop_solution
   python library_oop.py
   ```
