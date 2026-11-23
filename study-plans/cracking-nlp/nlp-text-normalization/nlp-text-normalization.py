import re

def text_normalize(text: str, operations: list) -> str:
    """
    Returns the normalized string.

    """
    
    for op in operations:
        if op == 'lowercase':
            text = text.lower()
        elif op == 'remove_punctuation':
            text = re.sub(r"[^\w\s]|_", "", text)
        elif op == 'remove_digits':
            text = re.sub(r"\d", "", text)
        elif op == 'collapse_whitespace':
            text = re.sub(r"\s+", " ", text)
        elif op == 'strip':
            text = text.strip()

    return text
            