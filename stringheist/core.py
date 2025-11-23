import re
import unicodedata
from typing import Any, Dict, Iterable, Tuple


# ---------- SLUGGING ----------

def slugify(
    s: str,
    *,
    allow_unicode: bool = False,
    sep: str = "-",
) -> str:
    """
    Convert a string to a URL-friendly slug.

    - Lowercases
    - Removes punctuation
    - Replaces spaces and separators with `sep`
    - Optionally normalizes to ASCII

    Examples:
        slugify("Hello, World!") -> "hello-world"
        slugify("Café au lait")  -> "cafe-au-lait" (default)
        slugify("Café au lait", allow_unicode=True) -> "cafe-au-lait"
    """
    if not s:
        return ""

    if not allow_unicode:
        s = unicodedata.normalize("NFKD", s)
        s = s.encode("ascii", "ignore").decode("ascii")
    else:
        s = unicodedata.normalize("NFKC", s)

    s = s.lower()
    # Replace any non-alphanumeric character with a separator
    s = re.sub(r"[^\w\s-]", "", s)
    # Replace whitespace or hyphens with a single separator
    s = re.sub(r"[-\s]+", sep, s).strip(sep)
    return s


# ---------- FUZZY MATCHING ----------

def _levenshtein_distance(a: str, b: str) -> int:
    """Compute the Levenshtein edit distance between two strings."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    prev_row = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr_row = [i]
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            curr_row.append(
                min(
                    prev_row[j] + 1,      # deletion
                    curr_row[j - 1] + 1,  # insertion
                    prev_row[j - 1] + cost,  # substitution
                )
            )
        prev_row = curr_row
    return prev_row[-1]


def similarity(a: str, b: str) -> float:
    """
    Return a similarity score between 0.0 and 1.0 based on Levenshtein distance.

    1.0 means identical strings, 0.0 means completely different.
    """
    if not a and not b:
        return 1.0
    dist = _levenshtein_distance(a, b)
    max_len = max(len(a), len(b))
    return 1.0 - dist / max_len


def best_match(
    query: str,
    choices: Iterable[str],
    *,
    cutoff: float = 0.0,
) -> Tuple[str | None, float]:
    """
    Return the best matching string from choices and its similarity score.

    If no match meets the cutoff, returns (None, 0.0).
    """
    best_item = None
    best_score = 0.0
    for c in choices:
        score = similarity(query, c)
        if score > best_score:
            best_item = c
            best_score = score
    if best_item is None or best_score < cutoff:
        return None, 0.0
    return best_item, best_score


# ---------- TEMPLATING ----------

_TEMPLATE_PATTERN = re.compile(r"{{\s*(?P<key>[\w\.]+)\s*}}")


def render_template(template: str, context: Dict[str, Any]) -> str:
    """
    Render a very small templating language using {{ key }} placeholders.

    Supports dotted keys for nested dict access, e.g. {{ user.name }}.

    Missing keys are left unchanged by default:
        "Hello, {{ name }}" with {} -> "Hello, {{ name }}"
    """

    def _resolve_key(path: str, ctx: Dict[str, Any]) -> Any:
        parts = path.split(".")
        value: Any = ctx
        for part in parts:
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return None
        return value

    def _replace(match: re.Match) -> str:
        key = match.group("key")
        value = _resolve_key(key, context)
        if value is None:
            # Leave as-is when not found
            return match.group(0)
        return str(value)

    return _TEMPLATE_PATTERN.sub(_replace, template)
