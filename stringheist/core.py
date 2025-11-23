"""Core string manipulation functions."""

import re
import unicodedata
from difflib import SequenceMatcher
from typing import Tuple, List, Optional, Dict, Any


def slugify(text: str) -> str:
    """
    Convert text to a URL-friendly slug.
    
    Args:
        text: The input text to slugify
        
    Returns:
        A lowercase slug with words separated by hyphens
    """
    # Normalize unicode characters to ASCII equivalents
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace non-alphanumeric characters with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    
    # Remove leading and trailing hyphens
    text = text.strip('-')
    
    return text


def similarity(str1: str, str2: str) -> float:
    """
    Calculate similarity between two strings using SequenceMatcher.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        Similarity score between 0.0 and 1.0
    """
    return SequenceMatcher(None, str1, str2).ratio()


def best_match(query: str, choices: List[str], cutoff: float = 0.6) -> Tuple[Optional[str], float]:
    """
    Find the best matching string from a list of choices.
    
    Args:
        query: The string to match
        choices: List of candidate strings
        cutoff: Minimum similarity score required (default 0.6)
        
    Returns:
        Tuple of (best_match, score) or (None, 0.0) if no match meets cutoff
    """
    if not choices:
        return None, 0.0
    
    best_score = 0.0
    best_choice = None
    
    for choice in choices:
        score = similarity(query, choice)
        if score > best_score:
            best_score = score
            best_choice = choice
    
    if best_score >= cutoff:
        return best_choice, best_score
    else:
        return None, 0.0


def render_template(template: str, context: Dict[str, Any]) -> str:
    """
    Simple template rendering with {{ variable }} syntax.
    
    Supports nested dictionary access using dot notation (e.g., {{ user.name }}).
    Missing keys are left intact in the output.
    
    Args:
        template: Template string with {{ variable }} placeholders
        context: Dictionary of values to substitute
        
    Returns:
        Rendered template string
    """
    def get_nested_value(data: Dict[str, Any], path: str) -> Any:
        """Get value from nested dictionary using dot notation."""
        keys = path.split('.')
        value = data
        
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return None
    
    def replace_var(match):
        """Replace a single variable match."""
        var_name = match.group(1).strip()
        value = get_nested_value(context, var_name)
        
        if value is not None:
            return str(value)
        else:
            # Leave the original placeholder intact if key is missing
            return match.group(0)
    
    # Find and replace all {{ variable }} patterns
    result = re.sub(r'\{\{\s*([^}]+)\s*\}\}', replace_var, template)
    
    return result
