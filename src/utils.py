import requests
from bs4 import BeautifulSoup

def get_text_from_url(url:str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator="\n", strip=True)

def get_text_from_file(path:str) -> str:
    with open(path) as file:
        return file.read()