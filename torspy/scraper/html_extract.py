#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import requests
from bs4 import BeautifulSoup

def check_onion_site(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        response = session.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        return False, f"Error fetching the page: {e}"

    if response.status_code == 200:
        return True, "Site exists and is reachable."
    else:
        return False, f"Site returned status code: {response.status_code}"

def extract_html(url):
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
    html_content = soup.prettify()
    print(html_content)
    
