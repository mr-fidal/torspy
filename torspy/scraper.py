#!/usr/bin/python3
# copyright (c) 2024 author Fidal

import os
import requests
from bs4 import BeautifulSoup
import sys

def check_tor_running():
    try:
        session = requests.session()
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        response = session.get('http://check.torproject.org', timeout=10)
        if "Congratulations. This browser is configured to use Tor." not in response.text:
            raise Exception("Tor is not properly configured.")
    except Exception as e:
        print("Error: Tor is not running or not properly configured. Please start Tor and try again.")
        sys.exit(1)

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

def find_directories(url, dir_file, save_file=None, save_directory=None):
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
        with open(dir_file, 'r') as file:
            directories = file.readlines()
    except IOError as e:
        print(f"Error reading the file: {e}")
        return

    found_directories = []
    for directory in directories:
        directory = directory.strip()
        test_url = os.path.join(url, directory)
        try:
            response = session.get(test_url, timeout=60)
            if response.status_code == 200:
                found_directories.append(test_url)
                print(f"Found: {test_url}")
        except requests.RequestException:
            continue

    if found_directories:
        print("\nFound directories:")
        for directory in found_directories:
            print(directory)
        
        if save_file:
            if save_directory:
                save_path = os.path.join(save_directory, save_file)
            else:
                save_path = save_file
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write('\n'.join(found_directories))
                print(f"Found directories saved to {save_path}")
            except IOError as e:
                print(f"Error saving the file: {e}")
    else:
        print("\nNo directories found.")
    
