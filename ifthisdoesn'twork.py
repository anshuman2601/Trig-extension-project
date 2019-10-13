import html2text
#import tempfile
#import shutil
import urllib.request
#import ssl

from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
#with urllib.request.urlopen('http://python.org/') as response:
    #with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        #shutil.copyfileobj(response, tmp_file)

#with open(tmp_file.name) as html:
    #pass

url = "https://genius.com/Ariana-grande-and-social-house-boyfriend-lyrics"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
info = urllib.request.urlopen(req).read()

def main():
    
    crimefile = open('fileName.txt','r')
    for line in crimefile.readlines():
        yourResult = line.split(',')
    
    crimefile2 = open('woah.txt','r')
    for line2 in crimefile2.readlines():
        yourResult2 = line2.split(',')
    
    return (len((set(yourResult)) & (set(yourResult2))))


    
