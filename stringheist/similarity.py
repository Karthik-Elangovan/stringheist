"""String similarity functions for comparing and matching strings."""


def levenshtein_distance(s1, s2):
    """
    Calculate the Levenshtein distance between two strings.
    
    Args:
        s1: First string
        s2: Second string
        
    Returns:
        The Levenshtein distance (number of edits needed)
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Cost of insertions, deletions, or substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]


def similarity(s1, s2):
    """
    Calculate the similarity between two strings.
    
    Returns a score between 0 and 1, where 1 is identical and 0 is completely different.
    
    Args:
        s1: First string
        s2: Second string
        
    Returns:
        Float similarity score between 0 and 1
    """
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    
    max_len = max(len(s1), len(s2))
    distance = levenshtein_distance(s1, s2)
    
    return 1.0 - (distance / max_len)


def best_match(query, choices):
    """
    Find the best matching string from a list of choices.
    
    Args:
        query: String to match against
        choices: List of strings to search through
        
    Returns:
        Tuple of (best_match_string, similarity_score)
    """
    if not choices:
        return None, 0.0
    
    best_score = 0
    best_choice = None
    
    for choice in choices:
        score = similarity(query, choice)
        if score > best_score:
            best_score = score
            best_choice = choice
    
    return best_choice, best_score
