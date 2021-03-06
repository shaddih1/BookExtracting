#!/usr/bin/env python3
# -.- coding: utf-8 -.-

import html5lib, urllib, re
from bs4 import BeautifulSoup

def webScan(url):
    returnlist = []
    html_page = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html_page, "html5lib")

    for l in soup.findAll('a', attrs={'href': re.compile("")}):
        returnlist.append(l.get('href'))

    return returnlist

def nameScan(url):
    # This function only works in feedbook
    # randomBook()
    html_page = urllib.request.urlopen(url).read().decode('utf-8')
    bsh = BeautifulSoup(html_page, 'html.parser')
    name = str(bsh.h1)

    return name[52:-5]
