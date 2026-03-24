import requests
from bs4 import BeautifulSoup
from .logger import get_logger

logger = get_logger('mirofish.url_parser')

def fetch_url_text(url: str) -> str:
    """Gets text content from a URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
            
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        logger.error(f"Error parsing URL {url}: {e}")
        return f"[Failed to scrape text from URL: {url}. Error: {e}]"
