from bs4 import BeautifulSoup
import html5lib
import urllib
import re

def getLinks(url):
    html_page = urllib.request.urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html_page, "html5lib")
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))

    return links, soup.name

print( getLinks("http://www.gutenberg.org/browse/authors/d#a5820") )