import unittest
from src.library import Library

class TestLibrary(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        self.assertIn("B1", lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("B1", "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Java", "James")
    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book("B2", "C++", "Bjarne")
        lib.borrow_book("B2")
        self.assertEqual(lib.books["B2"]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B3", "OS", "Tanenbaum")
        lib.borrow_book("B3")
        with self.assertRaises(ValueError):
            lib.borrow_book("B3")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B4", "DBMS", "Silberschatz")
        lib.borrow_book("B4")
        lib.return_book("B4")
        self.assertEqual(lib.books["B4"]["status"], "Available")
    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book(self):
        lib = Library()
        lib.add_book("B5", "Networks", "Kurose")
        report = lib.generate_report()
        self.assertIn("B5", report)
if __name__== "__main__":
    unittest.main()
