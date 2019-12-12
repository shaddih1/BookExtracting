# BookExtracting

![version](https://img.shields.io/badge/version-0.1-yellow.svg)
![language](https://img.shields.io/badge/language-python3%2B-green.svg)

## Description
Extract EPUBs, DOCXs, PDFs
## Banner

        _______
       /      /,    
      /      //   Book Extracting
     /______//          
    (______(/  V 0.1R   EPUB | DOCX
                            PDF
     
     # Coded By Shady H & Guy U
   
## Usage
    usage: book.py [-h] [-q] [-u URL] [-f NAME] {pdf,epub,docx}
        
    positional arguments:
      {pdf,epub,docx}       Extension type
            
    optional arguments:
      -h, --help            show this help message and exit
      -q, --quiet           Suppress warnings and chit-chat
      -u URL, --url URL     Set URL to extract
      -f NAME, --file_name NAME
                            Set file name
    example:
      $ python3 extracting.py -u http//:url... -f file_name pdf
      $ python3 extracting.py -q -u http://url... -f file_name epub
      $ python3 extracting.py
