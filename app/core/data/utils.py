import re

def clean_html(raw_html:str):
    if isinstance(raw_html, bytes):
        raw_html = raw_html.decode('utf-8')  # Decode bytes to string

    # Remove CSS classes and inline styles (via 'class' and 'style' attributes)
    raw_html = re.sub(r'\s*class=["\'][^"\']*["\']', '', raw_html)  # Remove class="..."
    raw_html = re.sub(r'\s*style=["\'][^"\']*["\']', '', raw_html)  # Remove style="..."

    # Remove specific unwanted tags like span, ul, ol, li, and any other tags.
    raw_html = re.sub(r'</?(span|ul|ol|li)[^>]*>', '', raw_html)

    # Remove incomplete or malformed HTML tags (tags starting with '<' but are incomplete or malformed)
    raw_html = re.sub(r'<\s*[^>]*\s*[^a-zA-Z0-9\s>]+', '', raw_html)  # Match incomplete tags

    # Remove all HTML tags (everything inside '<' and '>')
    raw_html = re.sub(r'<.*?>', '', raw_html)

    # Remove extraneous '>' characters that aren't part of valid HTML tags
    raw_html = re.sub(r'>\s*', ' ', raw_html)  # Replace any standalone '>' with a space
    raw_html = raw_html.replace('<', ' ')  # Remove any standalone '<' characters

    # Remove unnecessary line breaks and blank spaces
    clean_text = re.sub(r'\s+', ' ', raw_html).strip()

    # Remove words starting with a dot followed by words and dashes (e.g., .word-word-word)
    clean_text = re.sub(r'\s?\.\w+(-\w+)*', '', clean_text)

    return clean_text