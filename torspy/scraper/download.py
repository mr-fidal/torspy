#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def download_content(url, save_directory=None):
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

    downloaded_files = []
    for link in links:
        file_url = urljoin(url, link['href'])
        file_name = os.path.basename(file_url)

        if save_directory:
            save_path = os.path.join(save_directory, file_name)
        else:
            save_path = file_name

        try:
            file_response = session.get(file_url, timeout=60)
            file_response.raise_for_status()
            with open(save_path, 'wb') as file:
                file.write(file_response.content)
            downloaded_files.append(save_path)
            print(f"Downloaded: {save_path}")
        except requests.RequestException as e:
            print(f"Error downloading the file {file_name}: {e}")

    if downloaded_files:
        print("\nDownloaded files:")
        for file in downloaded_files:
            print(file)
    else:
        print("\nNo files were downloaded.")
        
