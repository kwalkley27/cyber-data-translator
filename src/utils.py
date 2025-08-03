import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException, Timeout
from bs4 import BeautifulSoup

def get_text_from_url(url:str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(separator="\n", strip=True)
    except ConnectionError:
        print("Failed to connect to the server")
    except Timeout:
        print("Request timed out")
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
        print(f"Status code: {response.status_code}")
    except RequestException as e:
        print(f"An error occurred: {e}")

def get_text_from_file(path:str) -> str:
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{path}' not found")
    except PermissionError:
        print(f"Permission denied to read file: {path}")
    except IOError as e:
        print(f"Error reading file: {e}")