#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# standard library
import requests, argparse, time, sys, os
from time import sleep

def usage():
	parser = argparse.ArgumentParser()
	parser.add_argument("extension", choices=['pdf','epub','docx'],
	    help="extension type")
	parser.add_argument("-q", "--quiet", action="store_true",
	    help="suppresses banner")
	parser.add_argument("-u", "--url", metavar="URL", help="set URL to extract")
	parser.add_argument("-p", "--path", metavar="PATH", help="set the document path")
	parser.add_argument("-f", "--file_name", metavar="FILE_NAME", help="set file name")
	if len(sys.argv) < 2:
		print("Comming Soon v0.2")
		sys.exit(0)
	return parser.parse_args()

def main():
	args = usage()
	if args.path:
		path = str(args.path)
	else:
		path = os.getcwd()
	if args.quiet:
		pass
	else:
		banner()
	url = args.url
	file_name = args.file_name
	extension = args.extension
	file = requests.get(url)
	try:
		open(path + "/{}.{}".format(file_name, extension), "wb").write(file.content)
		print("==> It has done successfully")
	except FileNotFoundError:
		print("Error: Set a correct path for the file")

def banner():
	print(""" _____         _   _____     _           _       _
| __  |___ ___| |_|   __|_ _| |_ ___ ___| |_ ___|_|___ ___
| __ -| . | . | '_|   __|_'_|  _|  _| .'|  _|  _| |   | . |
|_____|___|___|_,_|_____|_,_|_| |_| |__,|_| |___|_|_|_|_  |
                                                      |___| v0.2
			   # Coded by Shady H & Guy U
""")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
