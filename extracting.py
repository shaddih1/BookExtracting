#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# standard library
import requests, argparse, time, scan, random, sys, os
from time import sleep

def usage():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", metavar="URL", help="set URL to extract")
	parser.add_argument("-q", "--quiet", action="store_true",
	    help="suppresses banner")
	parser.add_argument("-p", "--path", metavar="PATH", help="set the document path")
	parser.add_argument("-r", "--random", action="store_true",
		help="download a random book of feedbook")
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
	print("[i] - Thanks for using BookExtracting")
	os._exit(0)

def interactive():
	menu = {
		"1" : randomBook,
		"2" : extraction
	}
	# display heading - (banner)
	heading()
	exit = False
	while not exit:
		for number, functions in menu.items():
			message = "\n\t{} ~ {}".format(number, functions.__doc__)
			print(message)
		print("\texit\n")
		option = input("Choose option > ").lower()
		exit = option == "exit"

		function = menu.get(option)
		if function:
			function()
	else:
		shutdown()

def randomBook():
	"""Random Book"""
	random_number_book = random.randint(1,7405)
	url = "https://es.feedbooks.com/book/{}".format(str(random_number_book))
	download_url = "{}.epub".format(url)
	# download
	book = scan.nameScan(url)
	try:
		req = requests.get(download_url)
		with open("{}.epub".format(book), "wb") as file:
			file.write(req.content)
		print("\n[+] - {}.epub It has been downloaded\n".format(book))
	except Exception:
		print("\n[!] - Please try later")

def extraction():
	"""Extraction | Unfinished"""
	global non_http_links
	# call getLinks function
	getLinks()
	if len(http_links) != 0:
		for l, i in enumerate(http_links):
			req = requests.get(i)
			with open(path + "{}.pdf".format(l), "wb") as file:
				file.write(req.content)
			print("[+] - It has been downloaded")
	elif len(non_http_links) != 0:
		if non_http_links[0] == '../':
			non_http_links = non_http_links[1:]
		for l, i in enumerate(non_http_links):
			print(i)
			req = requests.get(url + i)
			with open(path + "{}.pdf".format(l), "wb") as file:
				file.write(req.content)
			print("[+] - It has been downloaded")

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
                                    v0.2 unfinished   |___|
  BookExtracting | Coded by Shady H & Ulrich | Random mode
     {Designed to automate book extraction} Unfinished\n""")

def main():
	global url, path
	args = usage()
	if checkConnection():
		if args.random:
			randomBook()
			shutdown()
		url = args.url
		if args.path:
			path = args.path
		else:
			path = os.getcwd()
		if not args.quiet:
			heading()
		extraction()
	else:
		os._exit(1)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os._exit(0)
