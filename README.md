# BookExtracting

![version](https://img.shields.io/badge/version-0.2-yellow.svg)
![language](https://img.shields.io/badge/language-python3%2B-blue.svg)
[![GitHub license](https://img.shields.io/github/license/shaddih1/BookExtracting.svg)](https://github.com/shaddih1/BookExtracting/blob/master/LICENSE)

## Heading
          _____         _   _____     _               _   _
         | __  |___ ___| |_|   __|_ _| |_ ___ ___ ___| |_|_|___ ___
         | __ -| . | . | '_|   __|_'_|  _|  _| .'|  _|  _| |   | . |
         |_____|___|___|_,_|_____|_,_|_| |_| |__,|___|_| |_|_|_|_  |
                                             v0.2 unfinished   |___|
           BookExtracting | Coded by Shady H & Ulrich | Random mode
              {Designed to automate book extraction} Unfinished

## About 
Designed to automate book extraction, unfinished 
- Interactive menu
- Random Book mode it's now realised 

Coded with <3 for you, by Shady H & Ulrich

## How to install
Open the terminal and type following commands.

- $ apt install python-pip
- $ git clone https://github.com/shaddih1/BookExtracting.git
- $ cd BookExtracting
- $ pip install -r requirements.txt


## Usage
     usage: extracting.py [-h] [-u URL] [-q] [-p PATH] [-r]

     optional arguments:
       -h, --help            show this help message and exit
       -u URL, --url URL     set URL to extract
       -q, --quiet           suppresses banner
       -p PATH, --path PATH  set the document path
       -r, --random          download a random book of feedbook
      
 Example usage:
 
      $ python3 extracting.py -u http//:url... 
      $ python3 extracting.py -q -u http://url... 
      $ python3 extracting.py -q -u http//url... -p /user/name/...
      $ python3 extracting.py -r
      $ python3 extracting.py 
