import unittest
from bs4 import BeautifulSoup
from typed_soup import TypedSoup


class TestTypedSoup(unittest.TestCase):
    def test_find(self):
        html = "<div class='example'>Hello</div>"
        soup = BeautifulSoup(html, "html.parser")
        typed_soup = TypedSoup(soup)
        element = typed_soup.find("div", class_="example")
        self.assertIsNotNone(element)
        if element:
            self.assertEqual(element.get_text(), "Hello")

    def test_find_all(self):
        html = "<p>First</p><p>Second</p>"
        soup = BeautifulSoup(html, "html.parser")
        typed_soup = TypedSoup(soup)
        elements = typed_soup.find_all("p")
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0].get_text(), "First")
        self.assertEqual(elements[1].get_text(), "Second")

    def test_implicit_find_all(self):
        html = "<p>First</p><p>Second</p>"
        soup = BeautifulSoup(html, "html.parser")
        typed_soup = TypedSoup(soup)
        elements = typed_soup("p")
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[0].get_text(), "First")
        self.assertEqual(elements[1].get_text(), "Second")

if __name__ == "__main__":
    unittest.main()
