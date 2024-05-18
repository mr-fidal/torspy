#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import os
import requests
from bs4 import BeautifulSoup
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def extract_links(url, save_file=None, save_directory=None):
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
    links = soup.find_all('a', href=True)

    extracted_links = [link['href'] for link in links]
    
    print("Extracted links:")
    for link in extracted_links:
        print(link)

    if save_file:
        if save_directory:
            save_path = os.path.join(save_directory, save_file)
        else:
            save_path = save_file

        try:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write('\n'.join(extracted_links))
            print(f"Links saved to {save_path}")
        except IOError as e:
            print(f"Error saving the file: {e}")
    
