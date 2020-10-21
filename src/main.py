#!/usr/bin/env python3

import requests
import regex as re
import pdb

def keyword_worm(domain, url_path: str, found_urls={}) -> None:
    # search for all urls in the HTML page
    url_search = re.compile(r'https?://[\w@-]+\.[^/]+(?:/[\w-]+)+')
    
    get = requests.get(url_path)

    html = get.text

    for m in re.finditer(url_search, html):
        url = m.group()
        print(url)

        # ensure that we don't revisit a url we visited in the past
        if url not in found_urls:
            found_urls[url] = True

            keyword_worm(url, found_urls)

def main():
    url_path = 'https://food-guide.canada.ca/en/'

    keyword_worm(url_path)

if __name__ == '__main__':
    main()
