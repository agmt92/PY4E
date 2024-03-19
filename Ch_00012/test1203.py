# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
for i in range(7):
    mails = []
    url = input('Enter - ')
    response = urllib.request.urlopen(url, context=ctx)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    #print(tags)
    for tag in tags:
        mail = (tag.get('href', None))
        if mail:
            mails.append(mail)
    print(mails[17])
    # Close the response
    response.close()
