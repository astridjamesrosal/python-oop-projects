import unittest
from library_system import Book

class TestBook(unittest.TestCase):

    def test_borrow_available_book(self):
        book = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        result = book.borrow()
        self.assertEqual(result, True)              #Needs both assert for the result and state change because one passing doesn't guarantee the other.
        self.assertEqual(book.is_available, False)

    def test_borrow_already_borrowed_book(self):
        book = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        book.borrow()
        result = book.borrow()
        self.assertEqual(result, False)
        self.assertEqual(book.is_available, False)

    def test_return_borrowed_book(self):
        book = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        book.borrow()
        result = book.return_book()
        self.assertEqual(result, True)
        self.assertEqual(book.is_available, True)

    def test_return_available_book(self):
        book = Book(1, "Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        result = book.return_book()
        self.assertEqual(result, False)
        self.assertEqual(book.is_available, True)

if __name__ == "__main__":
    unittest.main()