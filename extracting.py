#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# standard library
import requests, argparse, time, sys, os
from time import sleep

def usage():
	parser = argparse.ArgumentParser(description="Book Extracting Tool.")
	parser.add_argument("-q", "--quiet", action="store_true",
	    help="Suppress warnings and chit-chat")
	parser.add_argument("-u", "--url", action="store_true", metavar="URL",
	    help="Set URL to extract")
	parser.add_argument("-f", "--file_name", action="store_true", metavar="FILE_NAME",
	    help="Set file name")
	parser.add_argument("-e", "--extension", choise="['pdf','epub','docx']",
	    help="Extension type")
	if len(sys.argv) < 2:
		print("Comming Soon")
		sys.exit()
	return parser.parse_args()

def main():
	args = usage()
	banner(args.quiet)
	url = args.url
	file_name = args.file_name
	extension = args.extension
	file = requests.get(url)
	open(os.getcwd() + "/{}.{}".format(name, extension), "wb").write(file.content)
	print("It has been done successfully.")


def banner():
	if not quiet:
		os.system('clear')
		print("""       _______
      /      /,
     /      //   Book Extracting
    /______//
   (______(/  V 0.1R   PDF

   # Coded By Shady H & Guy U
""")

if __name__ == "__main__":
	if sys.version_info.major < 3:
		print("Book Extracting supports only python3.")
		sys.exit(0)
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
