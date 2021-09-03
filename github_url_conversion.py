#!/bin/env python3
import re
"""Import Regular Expression Operations
A regular expression (or RE) specifies a set of strings that matches it; 
the functions in this module let you check if a particular string matches 
a given regular expression (or if a given regular expression matches a 
particular string, which comes down to the same thing).
https://docs.python.org/3/library/re.html
"""

def format_urls(filename):
    """Github URL Conversion
    
    This is a simple function that reads in a file containing Github URLs
    and converts them to simple Markdown format based on the ORG and REPO
    name, linking back to the full URL.
    
    Parameters
    ----------
    filename : str, required
        Text file containing list of Github URLs
    """
    file1 = open(filename,'r')
    while True:
        line = file1.readline()
        if not line:
                break
        url = re.sub('\n', r'', line, flags = re.M)
        org = re.sub('https:\/\/github.com\/', r'', url, flags = re.M)
        print("[" + org + "]" + "(" + url + ")")

format_urls('github_urls.txt')