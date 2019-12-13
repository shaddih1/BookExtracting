# BookExtracting

![version](https://img.shields.io/badge/version-0.1-yellow.svg)
![language](https://img.shields.io/badge/language-python3%2B-green.svg)

## Description
Designed to automate book extraction
## Banner

     _____         _   _____     _               _   _
    | __  |___ ___| |_|   __|_ _| |_ ___ ___ ___| |_|_|___ ___
    | __ -| . | . | '_|   __|_'_|  _|  _| .'|  _|  _| |   | . | 
    |_____|___|___|_,_|_____|_,_|_| |_| |__,|___|_| |_|_|_|_  |
                                                          |___|
        BookExtracting | v0.2 | Coded by Shady H & Guy U
              Designed to automate book extraction
              

   
## Usage
    usage: book.py [-h] [-q] [-u URL] [-f NAME] {pdf,epub,docx}
        
    positional arguments:
      {pdf,epub,docx}       extension type
            
    optional arguments:
      -h, --help            show this help message and exit
      -q, --quiet           suppresses printer model determination
      -u URL, --url URL     set URL to extract
      -p PATH, --path PATH  set the document path
      -f NAME, --file_name NAME
                            set file name
 Example usage:
 
      $ python3 extracting.py -u http//:url... -f file_name pdf
      $ python3 extracting.py -q -u http://url... -f file_name epub
      $ python3 extracting.py -u htt//url... -p /user/name/... -f file_name pdf
      $ python3 extracting.py 
