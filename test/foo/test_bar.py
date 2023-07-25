import unittest
from foo import bar

class TestFoo(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(bar.pip, "pop")
