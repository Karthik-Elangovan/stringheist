"""
stringheist - String Playfull

A Python library for string manipulation utilities.
"""

import re
import unicodedata


def slugify(text):
    """
    Convert a string to a URL-friendly slug.
    
    Args:
        text (str): The string to convert to a slug.
    
    Returns:
        str: A slugified version of the input string.
    
    Examples:
        >>> slugify("Hello, World!")
        'hello-world'
        >>> slugify("This is a TEST!")
        'this-is-a-test'
    """
    # Normalize unicode characters
    text = unicodedata.normalize('NFKD', str(text))
    # Encode to ASCII and decode to remove non-ASCII characters
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Convert to lowercase
    text = text.lower()
    # Replace any sequence of non-alphanumeric characters with a single dash
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove leading and trailing dashes
    text = text.strip('-')
    
    return text


__all__ = ['slugify']
