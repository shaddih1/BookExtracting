#!/usr/bin/env python3
# -.- coding: utf-8 -.-

import html5lib, urllib, re
from bs4 import BeautifulSoup

def getLinks(url,):
    returnlist = []
    html_page = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html_page, "html5lib")

    for l in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        returnlist.append(l.get('href'))

    return returnlist
