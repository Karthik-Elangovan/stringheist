"""Tests for stringheist similarity functions."""

import unittest
import sys
import os

# Add parent directory to path to import stringheist
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stringheist import similarity, best_match


class TestSimilarity(unittest.TestCase):
    """Test cases for the similarity function."""
    
    def test_identical_strings(self):
        """Identical strings should have similarity of 1.0."""
        self.assertEqual(similarity("hello", "hello"), 1.0)
        self.assertEqual(similarity("test", "test"), 1.0)
    
    def test_completely_different(self):
        """Completely different strings should have low similarity."""
        score = similarity("abc", "xyz")
        self.assertLess(score, 0.5)
    
    def test_hello_hullo(self):
        """Test the example from the problem statement."""
        score = similarity("hello", "hullo")
        self.assertGreaterEqual(score, 0.8)
        self.assertEqual(score, 0.8)
    
    def test_empty_strings(self):
        """Test edge cases with empty strings."""
        self.assertEqual(similarity("", ""), 1.0)
        self.assertEqual(similarity("hello", ""), 0.0)
        self.assertEqual(similarity("", "world"), 0.0)
    
    def test_case_sensitive(self):
        """Similarity should be case-sensitive."""
        score = similarity("Hello", "hello")
        self.assertLess(score, 1.0)


class TestBestMatch(unittest.TestCase):
    """Test cases for the best_match function."""
    
    def test_appl_example(self):
        """Test the example from the problem statement."""
        match, score = best_match("appl", ["apple", "banana", "orange"])
        self.assertEqual(match, "apple")
        self.assertGreater(score, 0.5)
    
    def test_exact_match(self):
        """Test when there's an exact match."""
        match, score = best_match("banana", ["apple", "banana", "orange"])
        self.assertEqual(match, "banana")
        self.assertEqual(score, 1.0)
    
    def test_empty_choices(self):
        """Test with empty choices list."""
        match, score = best_match("test", [])
        self.assertIsNone(match)
        self.assertEqual(score, 0.0)
    
    def test_single_choice(self):
        """Test with a single choice."""
        match, score = best_match("hello", ["hello"])
        self.assertEqual(match, "hello")
        self.assertEqual(score, 1.0)
    
    def test_multiple_similar(self):
        """Test when multiple choices are similar."""
        match, score = best_match("cat", ["cats", "dog", "bird"])
        self.assertEqual(match, "cats")
        self.assertGreater(score, 0.5)


if __name__ == '__main__':
    unittest.main()
