import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout
from bs4 import BeautifulSoup

def get_text_from_url(url: str, parser: str) -> str:
    """Fetch and parse text content from a URL.

    Args:
        url: The URL to fetch content from
        parser: The BeautifulSoup parser to use (e.g., 'html.parser', 'html5lib')

    Returns:
        Extracted text content from the URL

    Raises:
        ConnectionError: If unable to connect to the server
        Timeout: If the request times out
        HTTPError: If an HTTP error occurs
        RequestException: For other request-related errors
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, parser)
        return soup.get_text(separator="\n", strip=True)
    except ConnectionError as e:
        raise ConnectionError(f"Failed to connect to the server at {url}") from e
    except Timeout as e:
        raise Timeout(f"Request to {url} timed out") from e
    except HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}. Status code: {e.response.status_code}") from e
    except RequestException as e:
        raise RequestException(f"An error occurred while fetching {url}: {e}") from e

def get_text_from_file(path: str) -> str:
    """Read text content from a file.

    Args:
        path: Path to the file to read

    Returns:
        The file's text content

    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If lacking permission to read the file
        IOError: For other I/O errors
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File '{path}' not found") from e
    except PermissionError as e:
        raise PermissionError(f"Permission denied to read file: {path}") from e
    except IOError as e:
        raise IOError(f"Error reading file {path}: {e}") from e