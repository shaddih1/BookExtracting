#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# library
import requests, time, sys, os
from time import sleep

def main():
	if len(sys.argv) == 3:
		url = sys.argv[1]
		name = sys.argv[2]
		file = requests.get(url)
		banner()
		print("Stranting...")
		time.sleep(2)
		open(os.getcwd() + "/{}.pdf".format(name), "wb").write(file.content)
		print("It has been done successfully.")
	else:
		print("Usage: $ python3 extracting.py [url] [name]")

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