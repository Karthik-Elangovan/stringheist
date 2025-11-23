"""
Tests for the stringheist package
"""

import unittest
from stringheist import slugify


class TestSlugify(unittest.TestCase):
    """Test cases for the slugify function"""
    
    def test_hello_world(self):
        """Test the example from the problem statement"""
        result = slugify("Hello, World!")
        self.assertEqual(result, "hello-world")
    
    def test_lowercase_conversion(self):
        """Test that uppercase letters are converted to lowercase"""
        result = slugify("THIS IS A TEST")
        self.assertEqual(result, "this-is-a-test")
    
    def test_special_characters_removed(self):
        """Test that special characters are replaced with dashes"""
        result = slugify("Hello@World#2024!")
        self.assertEqual(result, "hello-world-2024")
    
    def test_multiple_spaces(self):
        """Test that multiple spaces are converted to a single dash"""
        result = slugify("Hello    World")
        self.assertEqual(result, "hello-world")
    
    def test_leading_trailing_spaces(self):
        """Test that leading and trailing spaces are removed"""
        result = slugify("  Hello World  ")
        self.assertEqual(result, "hello-world")
    
    def test_numbers_preserved(self):
        """Test that numbers are preserved in the slug"""
        result = slugify("Python 3.11")
        self.assertEqual(result, "python-3-11")
    
    def test_unicode_characters(self):
        """Test that unicode characters are handled properly"""
        result = slugify("Café")
        self.assertEqual(result, "cafe")
    
    def test_empty_string(self):
        """Test that an empty string returns an empty string"""
        result = slugify("")
        self.assertEqual(result, "")
    
    def test_only_special_characters(self):
        """Test that a string with only special characters returns empty string"""
        result = slugify("@#$%^&*()")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
