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

def interactive():
	# display heading (banner)
	heading()
	print("Comming soon")

def linkLists():
	global links, epub_links, pdf_links
	try:
		epub_links = []
		pdf_links = []
		# call getLinks function from scan.py
		links = scan.getLinks(url)
		for i in links:
			if ".epub" in i:
				epub_links.append(i)
			elif ".pdf" in i:
				pdf_links.append(i)
		# python3.6+ print(f"A total of {len(links)} links were found at {url}")
		print("A total of {} links were found at {}".format(len(links), url))
		if epub_links != []:
			# python3.6+ print(f" >>> {len(epub_links)} epub links found at {url}")
			print(" >>> {} epub links found at {}".format(len(epub_links), url))
		elif pdf_links != []:
			# python3.6+ print(f" >>> {len(pdf_links)} pdf links found at {url}")
			print(" >>> {} pdf links found at {}".format(len(pdf_links), url))
	except UnicodeDecodeError:
		print("Error [i] etc...")
		sys.exit()

def main():
	global url
	args = usage()
	if not args.quiet:
		heading()
	url = args.url
	linkLists()


def heading():
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
