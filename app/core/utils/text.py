import re

def clean_html(raw_html):
    """
    Remove HTML tags, unnecessary line breaks, and blank spaces from a string.

    Parameters:
    raw_html (str or bytes): The raw HTML string or bytes to clean.

    Returns:
    str: The cleaned text without HTML tags, unnecessary line breaks, and blank spaces.
    """
    if isinstance(raw_html, bytes):
        raw_html = raw_html.decode('utf-8')  # Decode bytes to string

    # Remove HTML tags
    clean_text = re.sub(r'<.*?>', '', raw_html)

    # Remove unnecessary line breaks and blank spaces
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    return clean_text