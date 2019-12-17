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
		print("Comming Soon v0.2")
	return parser.parse_args()

def main():
	global url, linkList
	args = usage()
	url = args.url
	for list in scan.getLinks(url):
		if website_name in list:
			linkList = list
	file = requests.get(url)
	if args.path:
		path = args.path
	else:
		path = os.getcwd()
	try:
		open(path + "/{}.{}".format(file_name, extension), "wb").write(file.content)

		print("==> It has done successfully")
	except FileNotFoundError:
		print("Error: Set a correct path for the file")

def banner():
	print(""" _____         _   _____     _               _   _
| __  |___ ___| |_|   __|_ _| |_ ___ ___ ___| |_|_|___ ___
| __ -| . | . | '_|   __|_'_|  _|  _| .'|  _|  _| |   | . |
|_____|___|___|_,_|_____|_,_|_| |_| |__,|___|_| |_|_|_|_  |
                                                      |___|
    BookExtracting | v0.2 | Coded by Shady H & Guy U
          Designed to automate book extraction
          """)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
