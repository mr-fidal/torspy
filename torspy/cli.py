#!/usr/bin/python3
# Copyright (©️) 2024 author: Fidal
# Issue : https://github.com/mr-fidal/torspy

import argparse
from .scraper.scrape import scrape_onion_site
from .scraper.directories import find_directories
from .scraper.subdomains import find_subdomains
from .scraper.html_extract import extract_html
from .scraper.analyze import analyze_content
from .scraper.download import download_content
from .scraper.links import find_links
from .scraper.services import get_service_info 

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
    parser.add_argument('--dir', type=str, help='The file containing directories to scan')
    parser.add_argument('--sub', type=str, help='The file containing subdomains to scan')
    parser.add_argument('--analyze', action='store_true', help='Analyze the content of the site')
    parser.add_argument('--download', action='store_true', help='Download the content of the site')
    parser.add_argument('--links', action='store_true', help='Find all links on the site')
    parser.add_argument('--service', action='store_true', help='Get service info of the site')

    args = parser.parse_args()

    if args.dir:
        find_directories(args.url, args.dir, args.save, args.directory)
    elif args.sub:
        find_subdomains(args.url, args.sub, args.save, args.directory)
    elif args.analyze:
        analyze_content(args.url, args.save, args.directory)
    elif args.download:
        download_content(args.url, args.save, args.directory)
    elif args.links:
        find_links(args.url, args.save, args.directory)
    elif args.service:
        get_service_info(args.url, args.save, args.directory)
    else:
        scrape_onion_site(args.url, args.find, args.save, args.directory)

if __name__ == "__main__":
    main()
