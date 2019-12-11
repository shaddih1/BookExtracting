#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# library
import requests, getopt, time, sys, os
from time import sleep

def usage():
	print("""Usage: $ python3 extracting.py [-u] url [-f] file_name

Information:
  -h, --help            Show this help message and exit
  -u, --url             Set URL to extract
  -f, --file_name       Set file name
  -e, --extension       Comming soon
  -s, --scan            Comming soon

Examples:
  $ python3 extracting.py -u url -f name
  $ python3 extracting.py --url url --file_name name""")

def main():
		# open(os.getcwd() + "/{}.pdf".format(name), "wb").write(file.content)
		# print("It has been done successfully.")
		

def banner():
	os.system('clear')
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
