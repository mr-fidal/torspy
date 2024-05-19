#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import requests
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
        print("Error : Tor is not running or not properly configured. Please start Tor and try again.")
        sys.exit(1)
