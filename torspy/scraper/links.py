#!/usr/bin/python3
# copyright ©️ 2024 author Fidal
# Issue : https://github.com/mr-fidal/torspy

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def find_links(url, save_file=None):
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
    links = set()
    
    for link in soup.find_all('a', href=True):
        full_url = urljoin(url, link['href'])
        links.add(full_url)

    print("Found links:")
    for link in links:
        print(f"Link: {link}")

    if save_file:
        with open(save_file, 'w') as f:
            for link in links:
                f.write(f"Link: {link}\n")
        print(f"Links saved to {save_file}")
