#step 1 importing the items

import requests
from bs4 import BeautifulSoup
import os

def wikipage_parser():
    url = "https://en.wikipedia.org/wiki/india"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    result= soup.findAll('div')
    for div in result:
        R1=div.find('h1')
    get_data(url)

def get_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    body = soup.find('h1')
    print(body.text)

if __name__ == "__main__":
    wikipage_parser()