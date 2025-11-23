"""
stringheist

A Python library for advanced string manipulation:
- Slugging
- Fuzzy matching
- Simple templating
"""

from .core import (
    slugify,
    similarity,
    best_match,
    render_template,
)

__all__ = [
    "slugify",
    "similarity",
    "best_match",
    "render_template",
]

__version__ = "0.1.0"
