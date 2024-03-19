from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
tot = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags span
tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    contint = int(tag.text)
    tot = tot + contint
print(tot)
