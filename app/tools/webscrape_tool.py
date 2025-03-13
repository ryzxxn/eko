import requests #type:ignore
from bs4 import BeautifulSoup #type:ignore

from core.utils.text import clean_html #type:ignore

def scrape_wikipedia(url):
    """
    Scrape a Wikipedia page to extract the title and the first paragraph.

    Parameters:
    - url: str : The URL of the Wikipedia page to scrape.

    Returns:
    - dict : A dictionary containing the title and the first paragraph of the article.
    """
    # Send a GET request to the Wikipedia page
    response = requests.get(url)

    print(response.content)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    
    cleaned_text = clean_html(response.content)

    return cleaned_text
