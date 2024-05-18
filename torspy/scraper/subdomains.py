# torspy/scraper/subdomains.py

import requests
from .tor_check import check_tor_running
from .html_extract import check_onion_site

def find_subdomains(url, sub_file, save_file=None, save_directory=None):
    check_tor_running()
    site_exists, message = check_onion_site(url)
    if not site_exists:
        print(message)
        return

    # Extract base URL for subdomain construction
    base_url = url.split("://")[-1]  # Get everything after "://"

    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        with open(sub_file, 'r') as file:
            subdomains = file.readlines()
    except IOError as e:
        print(f"Error reading the file: {e}")
        return

    found_subdomains = []
    for subdomain in subdomains:
        subdomain = subdomain.strip()
        test_url = f"http://{subdomain}.{base_url}"
        try:
            response = session.get(test_url, timeout=60)
            if response.status_code == 200 and (
                "index.html" in response.text or "index.php" in response.text
            ):
                found_subdomains.append(test_url)
                print(f"Found: {test_url}")
        except requests.RequestException:
            continue

    if found_subdomains:
        print("\nFound subdomains:")
        for sub in found_subdomains:
            print(sub)

        if save_file:
            if save_directory:
                save_path = os.path.join(save_directory, save_file)
            else:
                save_path = save_file
            try:
                with open(save_path, 'w', encoding='utf-8') as file:
                    file.write('\n'.join(found_subdomains))
                print(f"Found subdomains saved to {save_path}")
            except IOError as e:
                print(f"Error saving the file: {e}")
    else:
        print("\nNo subdomains found.")
