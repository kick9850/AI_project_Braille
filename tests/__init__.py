# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import unittest
from . import test_converter

class TestH2B(unittest.TestCase):

    def test_hangul_to_braille(self):
        self.assertTrue(test_converter.test_hangul_to_braille())

    def test_text_non_hangul_to_braille(self):
        self.assertTrue(test_converter.test_non_hangul_to_braille())

if __name__ == '__main__':
    unittest.main()