#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import requests
from bs4 import BeautifulSoup
from collections import Counter
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def analyze_content(url):
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
    text = soup.get_text()
    words = text.split()
    word_count = Counter(words)

    print("Word frequencies:")
    for word, count in word_count.most_common():
        print(f"{word}: {count}")
  
