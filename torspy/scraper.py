#!/usr/bin/python3
# copyright ©️ 2024 author Fidal 

import os
import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_session(proxy=None, user_agent=None):
    session = requests.Session()
    session.proxies = {
        'http': proxy if proxy else 'socks5h://127.0.0.1:9050',
        'https': proxy if proxy else 'socks5h://127.0.0.1:9050'
    }
    if user_agent:
        session.headers.update({'User-Agent': user_agent})
    return session

def check_onion_site(url, session):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    try:
        response = session.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching the page: {e}")
        return False, f"Error fetching the page: {e}"

    if response.status_code == 200:
        return True, "Site exists and is reachable."
    else:
        logger.warning(f"Site returned status code: {response.status_code}")
        return False, f"Site returned status code: {response.status_code}"

def scrape_onion_site(url, search_query=None, save_file=None, save_directory=None, proxy=None, user_agent=None):
    session = setup_session(proxy, user_agent)
    site_exists, message = check_onion_site(url, session)
    if not site_exists:
        logger.info(message)
        return

    try:
        response = session.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching the page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    if search_query:
        results = soup.find_all(string=lambda text: search_query.lower() in text.lower())
        result_content = '\n'.join([str(result.parent) for result in results])
        if save_file:
            save_path = os.path.join(save_directory, save_file) if save_directory else save_file
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(result_content)
                logger.info(f"Content matching '{search_query}' saved to {save_path}")
            except IOError as e:
                logger.error(f"Error saving the file: {e}")
        else:
            print(result_content)
    else:
        html_content = soup.prettify()
        if save_file:
            save_path = os.path.join(save_directory, save_file) if save_directory else save_file
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write(html_content)
                logger.info(f"HTML content saved to {save_path}")
            except IOError as e:
                logger.error(f"Error saving the file: {e}")
        else:
            print(html_content)
    
