# Import required modules
import os
import random
import string
import time
import sys
from bs4 import BeautifulSoup as BSHTML
import urllib.request
from urllib.request import urlopen

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# Define values for N and L, which determine the length of the two letters and four numbers in the prnt.sc

N=2
L=4
while True:
    twoletter = ''.join(random.choice(string.ascii_lowercase + string.ascii_lowercase) for N in range(N))
    fournumber = ''.join(random.choice(string.digits + string.digits) for L in range(L))

    # Join letters and numbers to form URL ID

    id = ''.join(twoletter + fournumber)

    # Create the url

    url_base = 'http://www.prnt.sc/'
    url_complete = ''.join(url_base + id)
    print("---------")

    # --------------------

    req = urllib.request.Request(url_complete, headers=hdr)
    page = urlopen(req)
    soup = BSHTML(page, features="html.parser")
    images = soup.findAll('img')
    url_list = []
    for image in images:
        src_get = image['src']
        url_list.append(src_get)
    iwantthatone = url_list[0]


    print("\033[1;33;40mTrying URL: " + url_list[0] + "\u001b[0m")
    if "image.prntscr.com" in url_list[0]:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(iwantthatone, id)
        pre, ext = os.path.splitext(id)
        os.rename(id, id + ".png")
        print("\033[1;32;40mSuccess!" + "\u001b[0m")

    else:
        print("\033[1;31;40mScreenshot is removed or it does not exist. We will ignore that."+"\u001b[0m")
        time.sleep(0.5)
        continue
