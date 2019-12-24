#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# standard library
import requests, argparse, time, scan, sys, os
from time import sleep

def usage():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", metavar="URL", help="set URL to extract")
	parser.add_argument("-q", "--quiet", action="store_true",
	    help="suppresses banner")
	parser.add_argument("-p", "--path", metavar="PATH", help="set the document path")
	if len(sys.argv) < 2:
		interactive()
	return parser.parse_args()

def shutdown():
	print("Some")
	os._exit(1)

def interactive():
	# display heading - (banner)
	heading()
	print("Comming soon")

def extraction():
	# links
	getLinks()
	if len(http_links) != 0:
		try:
			for l, i in enumerate(http_links):
				req = requests.get(i)
				with open(path + "/books/{}.pdf".format(l), "wb") as file:
					file.write(req.content)
				print("It was done")
		except FileNotFoundError:
			shutdown()
def getLinks():
	global non_http_links, http_links
	try:
		# call webScan function from scan.py
		links = scan.webScan(url)
		# links list classification
		if len(links) != 0:
			non_http_links = links
			http_links = []
			for i in links:
				if "http://" in i or "https://" in i:
					http_links.append(i)
			if len(http_links) != 0:
				for i in http_links:
					non_http_links.remove(i)
	except UnicodeDecodeError:
		shutdown()

def heading():
	print("""\n_____         _   _____     _               _   _
| __  |___ ___| |_|   __|_ _| |_ ___ ___ ___| |_|_|___ ___
| __ -| . | . | '_|   __|_'_|  _|  _| .'|  _|  _| |   | . |
|_____|___|___|_,_|_____|_,_|_| |_| |__,|___|_| |_|_|_|_  |
                                                      |___|
    BookExtracting | v0.2 | Coded by Shady H & Guy U
          Designed to automate book extraction""")

def main():
	global url
	args = usage()
	if not args.quiet:
		heading()
	url = args.url
	try:
		linkLists()
	except ValueError:
		shutdown()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os._exit(0)
