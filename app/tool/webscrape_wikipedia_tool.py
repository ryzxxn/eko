import requests  # type: ignore
import re
from bs4 import BeautifulSoup  # type: ignore

def scrape_wikipedia(*, topic: str, url: str = None):
    """
    Scrape a Wikipedia page to extract the title, all headers (h1, h2, h3), and paragraphs (p).

    Parameters:
    - topic: str : The Wikipedia topic or URL to scrape.
    - url: str (optional) : A direct Wikipedia URL, if provided, will be used.

    Returns:
    - dict : A dictionary containing the title and the text of the article.
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

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title
    title = soup.find('h1', {'id': 'firstHeading'}).text

    # Extract all text from h1, h2, h3, and p tags
    headers = soup.find_all(['h1', 'h2', 'h3'])
    paragraphs = soup.find_all('p')

    # Combine all text from headers and paragraphs
    all_text = []

    # Add headers text to the list
    for header in headers:
        all_text.append(header.get_text(strip=True))

    # Add paragraphs text to the list
    for paragraph in paragraphs:
        all_text.append(paragraph.get_text(strip=True))

    # Join all the text in the list into one string
    full_text = '\n'.join(all_text)

    return {
        "title": title,
        "content": full_text
    }
