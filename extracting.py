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

def checkConnection():
	try:
		# check internet connection with the requests module
		req = requests.get("https://google.com", timeout=4)
		return True
	except requests.ConnectionError:
		print("[Error] - Please check your internet connection.")
	return False

def shutdown():
	print("Some")
	os._exit(1)

def interactive():
	# display heading - (banner)
	heading()
	print("Comming soon")

def extraction():
	# call getLinks function
	getLinks()
	try:
		if len(http_links) != 0:
			for l, i in enumerate(http_links):
				req = requests.get(i)
				with open(path + "{}.pdf".format(l), "wb") as file:
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
    BookExtracting | v0.2 | Coded by Shady H & Ulrich
          Designed to automate book extraction""")

def main():
	global url, path
	args = usage()
	if checkConnection():
		url = args.url
		if args.path:
			path = args.path
		else:
			path = os.getcwd()
		if not args.quiet:
			heading()
		try:
			extraction()
		except ValueError:
			shutdown()
	else:
		os._exit(1)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os._exit(0)
