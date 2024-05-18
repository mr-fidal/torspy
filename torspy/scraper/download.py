import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def download_files(url, file_type, save_directory=None):
    check_tor_running()
    site_exists, message = check_onion_site(url)
    if not site_exists:
        print(message)
        return

    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        response = session.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    files = [urljoin(url, a['href']) for a in soup.find_all('a', href=True) if a['href'].endswith(file_type)]

    if not save_directory:
        save_directory = os.getcwd()

    os.makedirs(save_directory, exist_ok=True)

    for file_url in files:
        try:
            file_response = session.get(file_url, timeout=60)
            file_response.raise_for_status()
            file_name = os.path.join(save_directory, os.path.basename(file_url))
            with open(file_name, 'wb') as file:
                file.write(file_response.content)
            print(f"Downloaded: {file_name}")
        except requests.RequestException as e:
            print(f"Error downloading {file_url}: {e}")
  
