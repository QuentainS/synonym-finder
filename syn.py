#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import argparse


def get_syns(word):

    syns = []

    # Get the webpage
    html = requests.get("http://www.synonymes.com/synonyme.php?mot=" + word)
    soup = BeautifulSoup(html.text, 'html.parser')

    # Get all synonyms
    for elem in soup.find_all("div", {"class": "defbox"}):
        for a in elem.find_all('a'):
            syns.append(a.text)

    return syns


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find synonyms of a given word')
    parser.add_argument('word')
    args = parser.parse_args()

    try:
        syns = get_syns(args.word)
    except:
        print("[X] Error with website")

    if syns == []:
        print("[!] No result")
    else:
        [print(syn) for syn in syns]
