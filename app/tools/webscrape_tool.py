import requests  # type:ignore
from core.utils.text import clean_html  # type:ignore
import re

def scrape_wikipedia(*, topic: str, url: str = None):
    """
    Scrape a Wikipedia page to extract the title and the first paragraph.

    Parameters:
    - topic: str : The Wikipedia topic or URL to scrape.
    - url: str (optional) : A direct Wikipedia URL, if provided, will be used.

    Returns:
    - dict : A dictionary containing the cleaned text of the article.
    """
    # Check if the topic is a valid Wikipedia URL or a topic
    if re.match(r"^https?://(www\.)?wikipedia\.org/wiki/", topic):
        # If it's a valid URL, use it directly
        url = topic
    elif not url:
        # If it's a topic and no URL is provided, construct the Wikipedia URL
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"

    # Send a GET request to the Wikipedia page
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    
    # Clean the HTML content
    cleaned_text = clean_html(response.content)

    return cleaned_text
