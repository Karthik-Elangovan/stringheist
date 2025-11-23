"""
Core string manipulation functions for stringheist.
"""

import re
import unicodedata
from difflib import SequenceMatcher
from typing import Optional, List, Tuple, Dict, Any


def slugify(text: str, separator: str = "-") -> str:
    """
    Convert a string into a URL-friendly slug.
    
    Args:
        text: The text to slugify
        separator: The separator to use between words (default: "-")
    
    Returns:
        A slugified version of the input text
    
    Example:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify("Python 3.9 Rules!", separator="_")
        'python_3_9_rules'
    """
    # Normalize unicode characters
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace non-alphanumeric characters with separator
    text = re.sub(r'[^a-z0-9]+', separator, text)
    
    # Remove leading/trailing separators
    text = text.strip(separator)
    
    return text


def similarity(str1: str, str2: str) -> float:
    """
    Calculate the similarity between two strings using fuzzy matching.
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        A float between 0 and 1, where 1 is identical and 0 is completely different
    
    Example:
        >>> similarity("hello", "hallo")
        0.8
        >>> similarity("python", "python")
        1.0
    """
    return SequenceMatcher(None, str1, str2).ratio()


def best_match(query: str, choices: List[str], threshold: float = 0.6) -> Optional[Tuple[str, float]]:
    """
    Find the best match for a query string from a list of choices.
    
    Args:
        query: The string to match
        choices: List of strings to search through
        threshold: Minimum similarity score to consider (default: 0.6)
    
    Returns:
        A tuple of (best_match, score) or None if no match exceeds the threshold
    
    Example:
        >>> best_match("python", ["java", "python3", "ruby"])
        ('python3', 0.857...)
    """
    if not choices:
        return None
    
    best_score = 0.0
    best_string = None
    
    for choice in choices:
        score = similarity(query, choice)
        if score > best_score:
            best_score = score
            best_string = choice
    
    if best_score >= threshold:
        return (best_string, best_score)
    
    return None


def render_template(template: str, context: Dict[str, Any]) -> str:
    """
    Render a simple template with variable substitution.
    
    Args:
        template: Template string with {{variable}} placeholders
        context: Dictionary of variable names to values
    
    Returns:
        The rendered template string
    
    Example:
        >>> render_template("Hello {{name}}!", {"name": "World"})
        'Hello World!'
        >>> render_template("{{greeting}} {{name}}!", {"greeting": "Hi", "name": "Python"})
        'Hi Python!'
    """
    result = template
    
    for key, value in context.items():
        placeholder = f"{{{{{key}}}}}"
        result = result.replace(placeholder, str(value))
    
    return result
