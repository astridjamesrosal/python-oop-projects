import unittest
from library_system import Book, Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library("test_library.json")

    def tearDown(self):
        import os
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_add_book(self):
        self.library.add_book("Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Harry Potter")

    def test_borrow_book_success(self):
        self.library.add_book("Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        result = self.library.borrow_book(1)
        self.assertEqual(result, True)
        self.assertEqual(self.library.books[0].is_available, False)

    def test_borrow_book_failure(self):
        result = self.library.borrow_book(2)
        self.assertEqual(result, False)

    def test_return_book_success(self):
        self.library.add_book("Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        self.library.borrow_book(1)
        result = self.library.return_book(1)
        self.assertEqual(result, True)
        self.assertEqual(self.library.books[0].is_available, True)

    def test_return_book_failure(self):
        result = self.library.return_book(2)
        self.assertEqual(result, False)

    def test_search_by_title(self):
        self.library.add_book("Harry Potter", "J.K. Rowling", "Fantasy", 1991)
        result = self.library.search_by_title("Harry Potter")
        self.assertEqual(len(result), 1)
        self.assertEqual(self.library.books[0].title, "Harry Potter")

if __name__ == "__main__":
    unittest.main()