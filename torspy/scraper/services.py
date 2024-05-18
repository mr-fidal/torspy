import requests
from bs4 import BeautifulSoup
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def detect_services(url):
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
    services = []

    if soup.find('meta', {'name': 'generator', 'content': 'WordPress'}):
        services.append('WordPress')
    if soup.find('meta', {'name': 'generator', 'content': 'Drupal'}):
        services.append('Drupal')
    if 'phpMyAdmin' in response.text:
        services.append('phpMyAdmin')

    if services:
        print(f"Detected services: {', '.join(services)}")
    else:
        print("No specific services detected.")
                 
