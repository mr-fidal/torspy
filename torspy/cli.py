#!/usr/bin/python3
# copyright ©️ 2024 author Fidal 

import argparse
from .scraper import scrape_onion_site

def main():
    parser = argparse.ArgumentParser(prog='torspy', description='Tor onion site scraping tool')
    parser.add_argument('url', type=str, help='The .onion site URL to scrape')
    parser.add_argument('--find', type=str, help='The text to search for within the site')
    parser.add_argument('-s', '--save', type=str, help='The file name to save the content')
    parser.add_argument('-d', '--directory', type=str, help='The directory to save the file')
    args = parser.parse_args()
    scrape_onion_site(args.url, args.find, args.save, args.directory)

if __name__ == "__main__":
    main()
  