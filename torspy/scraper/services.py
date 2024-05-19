#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import requests
from .tor_check import check_tor_running
from .html_extract import check_onion_site
import os

def get_service_info(url, save_file=None, directory=None):
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

    headers = response.headers
    server_info = headers.get('Server', 'Unknown')

    extracted_services = f"Extracted services:\nServer: {server_info}"
    print(extracted_services)

    if save_file:
        if directory:
            save_path = os.path.join(directory, save_file)
        else:
            save_path = save_file
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(extracted_services)
        print(f"Service information saved to {save_path}")
