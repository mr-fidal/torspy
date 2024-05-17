#!/usr/bin/python3
# copyright ©️ 2024 author Fidal

import argparse
from .scraper import scrape_onion_site, find_directories, find_subdomains

def main():
    epilog_text = '''
Copyright (©️) 2024 author: Fidal
Issue: https://GitHub.com/mr-fidal/torspy
'''
    parser = argparse.ArgumentParser(description='Scrape a .onion site.', epilog=epilog_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('url', type=str, help='The .onion site URL to scrape')
    parser.add_argument('--find', type=str, help='The text to search for within the site')
    parser.add_argument('-s', '--save', type=str, help='The file name to save the content')
    parser.add_argument('-d', '--directory', type=str, help='The directory to save the file')
    parser.add_argument('--dir', type=str, help='File containing list of directories to check')
    parser.add_argument('--sub', type=str, help='File containing list of subdomains to check')
    args = parser.parse_args()

    if args.dir:
        find_directories(args.url, args.dir, args.save, args.directory)
    elif args.sub:
        find_subdomains(args.url, args.sub, args.save, args.directory)
    else:
        scrape_onion_site(args.url, args.find, args.save, args.directory)

if __name__ == "__main__":
    main()
    
