#!/usr/bin/python3
# copyright ©️ 2024 author Fidal
# Issue : https://github.com/mr-fidal/torspy

import requests
from bs4 import BeautifulSoup
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def get_service_info(url, save_file=None):
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

    service_info = []
    for script in soup.find_all('script'):
        if 'service' in script.text.lower():
            service_info.append(script.text.strip())

    print("Extracted services:")
    for info in service_info:
        print(info)

    if save_file:
        with open(save_file, 'w', encoding='utf-8') as f:
            for info in service_info:
                f.write(info + "\n")
        print(f"Services saved to {save_file}")
