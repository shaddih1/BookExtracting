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
	    help="suppresses printer model determination")
	parser.add_argument("-u", "--url", metavar="URL", help="set URL to extract")
	parser.add_argument("-p", "--path", metavar="PATH", help="set the document path")
	parser.add_argument("-f", "--file_name", metavar="FILE_NAME", help="set file name")
	if len(sys.argv) < 2:
		print("Comming Soon v0.2")
		sys.exit(0)
	return parser.parse_args()

def main():
	args = usage()
	if args.quiet:
		pass
	else:
		banner()
	if args.path:
		path = str(args.path)
	else:
		path = os.getcwd()
	url = args.url
	file_name = args.file_name
	extension = args.extension
	file = requests.get(url)
	try:
		open(path + "/{}.{}".format(file_name, extension), "wb").write(file.content)
		print("It has been done successfully.")
	except FileNotFoundError:
		print("Error: Set a correct path for the file")
		pass

def banner():
	print("""       _______
      /      /,
     /      //   Book Extracting
    /______//
   (______(/  V 0.1R   PDF

   # Coded By Shady H & Guy U
""")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
