# This is a box that contians several tools to parse text to words

# required packages:
from bs4 import BeautifulSoup
import re


def htmlToWords(webpage):

    # convert webpage to text
    text = BeautifulSoup(webpage, 'html5lib').get_text()
    # remove all none numalpha
    words = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    return words


def 
