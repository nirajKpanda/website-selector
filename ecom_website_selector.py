import requests
import re
import argparse
import pandas as pd
from bs4 import BeautifulSoup


"""
    A website to be a ecommerce site we find some common links like, 
    Cart, Checkout, TrackOrder, Wishlist, Shop
"""
def is_ecommerce_website(site):
    url = 'http://' + site

    """
        Incase we get any HTTP exception the wrapper will return false 
        for the given website
    """
    try:
        data = requests.get(url)
    except Exception as e:
        return

    soup = BeautifulSoup(data.content, 'html.parser')
    
    if soup.find_all('a', re.compile(r'cart|checkout|tarckorder|wishlist', re.IGNORECASE)):
        return True
    else:
        False


def main():
    parser = argparse.ArgumentParser(description="Script to test a website is ecommerce site or not!")
    parser.add_argument('-i',
            '--infile',
            help='Input file with all websites name to test',
            required=True
            )
    
    parser.add_argument('-o',
            '--outfile',
            help='Output csv file, where test result to be dumped',
            required=False
            )
    args = parser.parse_args()
    _infile = args.infile
    _outfile = args.outfile
    
    websites = []

    """
        Reading input file with all website names and
        appending to a list 
    """
    with open(_infile) as fp:
        data = fp.readlines()
        for website in data:
            websites.append(website.strip())

    """
        Iterating through each website and checking 
        wheather the site is ecommerce or not.
    """
    if not _outfile:
        print('website, e-commerce')
        print('-------------------')
        print
        
        for website in websites:
            if is_ecommerce_website(website):
                print('{}, {}'.format(website, 'true'))
            else:
                print('{}, {}'.format(website, 'false'))
    else:
        output = [('website', 'ecommerce')]
        
        for website in websites:
            if is_ecommerce_website(website):
                output.append((website, 'true'))
            else:
                output.append((website, 'false'))

        df = pd.DataFrame(output)
        df.to_csv(_output, index=False)


if __name__ == '__main__':
    main()
