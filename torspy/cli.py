#!/usr/bin/python3
# copyright ©️ 2024 author Fidal

import argparse
from .scraper.scrape import scrape_onion_site
from .scraper.directories import find_directories
from .scraper.subdomains import find_subdomains
from .scraper.services import detect_services
from .scraper.links import extract_links
from .scraper.analyze import analyze_content
from .scraper.download import download_files
from .scraper.screenshot import capture_screenshot

def main():
    epilog_text = '''
\ntorspy is a robust Python package fortified with powerful algorithms, designed for seamless exploration of .onion sites via the Tor network. Its arsenal includes adept scraping of HTML from .onion URLs, precise text localization within the acquired content, and proficient storage of findings. Moreover, torspy boasts formidable subdomain scanning capabilities, enabling thorough reconnaissance across diverse subdomains. Additionally, it excels at detecting hidden directories, further enhancing its efficacy in navigating and extracting valuable information from the depths of the dark web.\n\n
Copyright (c) 2024 author: Fidal
Report an Issue : https://github.com/mr-fidal/torspy/issues
    '''
    parser = argparse.ArgumentParser(description='Scrape a .onion site.', epilog=epilog_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('url', type=str, help='The .onion site URL to scrape')
    parser.add_argument('--find', type=str, help='The text to search for within the site')
    parser.add_argument('-s', '--save', type=str, help='The file name to save the content')
    parser.add_argument('-d', '--directory', type=str, help='The directory to save the file')
    parser.add_argument('--dir', type=str, help='File containing list of directories to check')
    parser.add_argument('--sub', type=str, help='File containing list of subdomains to check')
    parser.add_argument('--services', action='store_true', help='Detect services running on the onion site')
    parser.add_argument('--links', action='store_true', help='Extract all links from the onion site')
    parser.add_argument('--analyze', action='store_true', help='Analyze the content of the onion site')
    parser.add_argument('--download', type=str, help='Download specific types of files from the onion site')
    parser.add_argument('--screenshot', type=str, help='Capture a screenshot of the onion site')

    args = parser.parse_args()

    if args.dir:
        find_directories(args.url, args.dir, args.save, args.directory)
    elif args.sub:
        find_subdomains(args.url, args.sub, args.save, args.directory)
    elif args.services:
        detect_services(args.url)
    elif args.links:
        extract_links(args.url)
    elif args.analyze:
        analyze_content(args.url)
    elif args.download:
        download_files(args.url, args.download, args.directory)
    else:
        scrape_onion_site(args.url, args.find, args.save, args.directory)

if __name__ == "__main__":
    main()
    

    
