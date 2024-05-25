import io
import sys
import unittest

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize to None to ensure the setter is called
        self.set_page_count(page_count)

    def set_title(self, new_title):
        self.title = new_title

    def set_page_count(self, new_page_count):
        if isinstance(new_page_count, int):
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")

    def get_title(self):
        return self.title

    def get_page_count(self):
        return self._page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    # Ensure the property is used to call the setter method
    page_count = property(get_page_count, set_page_count)

class TestBook(unittest.TestCase):
    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"

if __name__ == "__main__":
    unittest.main()
