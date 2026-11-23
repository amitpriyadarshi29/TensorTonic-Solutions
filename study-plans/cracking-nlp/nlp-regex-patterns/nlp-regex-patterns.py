import re

PATTERNS = {
        "emails": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "urls": r"https?://\S+",
        "dates": r"\b(?:\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b",
        "money": r"\$\d+(?:\.\d{2})?",
        "hashtags": r"#\w+",
}
def extract_patterns(text: str, pattern_type: str) -> list:
    """
    Returns a list of matched strings.
    """
    matches = []
    if pattern_type not in PATTERNS:
        return []
    matches = re.findall(PATTERNS[pattern_type], text)

    if pattern_type == "urls":
        matches = [m.rstrip(",.)!?;:") for m in matches]

    return matches
