##from urllib.request import urlopen
#url = "https://investor.vanguard.com/search/?query=FLR"
#page = urlopen(url)
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")
#print(html)

import re
import urllib.request
response = urllib.request.urlopen('https://investor.vanguard.com/search/?query=FLR')
html = response.read()
text = html.decode()
re.findall('(.*?)',text)
print(text)

import requests
url=requests.get('http://example.webscraping.com/ajax/search.json?page=0&page_size=10&search_term=a')
url.json()