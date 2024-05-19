#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import os
import requests
from bs4 import BeautifulSoup
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def scrape_onion_site(url, search_query=None, save_file=None, save_directory=None):
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

    if search_query:
        results = soup.find_all(string=lambda text: search_query.lower() in text.lower())
        result_content = '\n'.join([str(result.parent) for result in results])
        if save_file:
            if save_directory:
                save_path = os.path.join(save_directory, save_file)
            else:
                save_path = save_file
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(result_content)
                print(f"Content matching '{search_query}' saved to {save_path}")
            except IOError as e:
                print(f"Error saving the file: {e}")
        else:
            print(result_content)
    else:
        html_content = soup.prettify()
        if save_file:
            if save_directory:
                save_path = os.path.join(save_directory, save_file)
            else:
                save_path = save_file
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(html_content)
                print(f"HTML content saved to {save_path}")
            except IOError as e:
                print(f"Error saving the file: {e}")
        else:
            print(html_content)
      
