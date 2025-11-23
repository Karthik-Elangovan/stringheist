"""
Unit tests for the stringheist library.
"""

import unittest
import sys
import os

# Add parent directory to path to import stringheist
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stringheist import slugify, similarity, best_match, render_template


class TestSlugify(unittest.TestCase):
    """Test the slugify function."""
    
    def test_basic_slugify(self):
        """Test basic slugification."""
        self.assertEqual(slugify("Hello World!"), "hello-world")
    
    def test_slugify_with_numbers(self):
        """Test slugification with numbers."""
        self.assertEqual(slugify("Python 3.9 Rules!"), "python-3-9-rules")
    
    def test_slugify_custom_separator(self):
        """Test slugification with custom separator."""
        self.assertEqual(slugify("Python 3.9 Rules!", separator="_"), "python_3_9_rules")
    
    def test_slugify_unicode(self):
        """Test slugification with unicode characters."""
        result = slugify("Café au Lait")
        self.assertEqual(result, "cafe-au-lait")
    
    def test_slugify_special_chars(self):
        """Test slugification removes special characters."""
        self.assertEqual(slugify("Hello@World#Test!"), "hello-world-test")


class TestSimilarity(unittest.TestCase):
    """Test the similarity function."""
    
    def test_identical_strings(self):
        """Test similarity of identical strings."""
        self.assertEqual(similarity("python", "python"), 1.0)
    
    def test_similar_strings(self):
        """Test similarity of similar strings."""
        score = similarity("hello", "hallo")
        self.assertAlmostEqual(score, 0.8, places=1)
    
    def test_different_strings(self):
        """Test similarity of different strings."""
        score = similarity("python", "java")
        self.assertLess(score, 0.5)
    
    def test_empty_strings(self):
        """Test similarity with empty strings."""
        self.assertEqual(similarity("", ""), 1.0)


class TestBestMatch(unittest.TestCase):
    """Test the best_match function."""
    
    def test_best_match_found(self):
        """Test finding the best match."""
        result = best_match("python", ["java", "python3", "ruby"])
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "python3")
        self.assertGreater(result[1], 0.8)
    
    def test_best_match_with_threshold(self):
        """Test best match with custom threshold."""
        result = best_match("python", ["java", "ruby"], threshold=0.9)
        self.assertIsNone(result)
    
    def test_best_match_empty_list(self):
        """Test best match with empty list."""
        result = best_match("python", [])
        self.assertIsNone(result)
    
    def test_best_match_exact(self):
        """Test best match with exact match."""
        result = best_match("python", ["java", "python", "ruby"])
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "python")
        self.assertEqual(result[1], 1.0)


class TestRenderTemplate(unittest.TestCase):
    """Test the render_template function."""
    
    def test_basic_template(self):
        """Test basic template rendering."""
        result = render_template("Hello {{name}}!", {"name": "World"})
        self.assertEqual(result, "Hello World!")
    
    def test_multiple_variables(self):
        """Test template with multiple variables."""
        result = render_template("{{greeting}} {{name}}!", {"greeting": "Hi", "name": "Python"})
        self.assertEqual(result, "Hi Python!")
    
    def test_template_with_numbers(self):
        """Test template with number values."""
        result = render_template("Version {{version}}", {"version": 3.9})
        self.assertEqual(result, "Version 3.9")
    
    def test_missing_variable(self):
        """Test template with missing variable."""
        result = render_template("Hello {{name}}!", {})
        self.assertEqual(result, "Hello {{name}}!")
    
    def test_no_variables(self):
        """Test template with no variables."""
        result = render_template("Hello World!", {})
        self.assertEqual(result, "Hello World!")


if __name__ == "__main__":
    unittest.main()
