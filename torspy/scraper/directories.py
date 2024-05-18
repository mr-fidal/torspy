#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue: https://github.com/mr-fidal/torspy

import os
import requests
from .tor_check import check_tor_running
from .html_extract import check_onion_site

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
            if response.status_code == 200 and (
                "index.html" in response.text or "index.php" in response.text or 
                "login.html" in response.text or "login.php" in response.text or 
                "home.html" in response.text or "home.php" in response.text or 
                "main.html" in response.text or "main.php" in response.text or 
                "about.html" in response.text or "contact.html" in response.text or 
                "contact.php" in response.text or "form.html" in response.text or 
                "form.php" in response.text or "register.html" in response.text or 
                "register.php" in response.text or "signup.html" in response.text or 
                "signup.php" in response.text or "dashboard.html" in response.text or 
                "dashboard.php" in response.text or "admin.html" in response.text or 
                "admin.php" in response.text or "logout.html" in response.text or 
                "404.html" in response.text or "style.css" in response.text or 
                "styles.css" in response.text or "script.js" in response.text or 
                "database.db" in response.text or "app.db" in response.text or 
                "main.db" in response.text or "web.db" in response.text or 
                "users.db" in response.text or "web.db" in response.text or 
                "customer.db" in response.text or "inventory.db" in response.text
            ):
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
