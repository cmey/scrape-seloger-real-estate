# Base on https://flothesof.github.io/paris-appartment-prices.html

url = 'http://www.seloger.com/list.htm?org=advanced_search&idtt=1&idtypebien=1&cp=75&tri=initial&nb_pieces=2&naturebien=1,2,4'

headers = {'User-Agent': '*',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'}


import requests

s = requests.Session()
s.headers.update(headers)
r = s.get(url)
r
# 403. We get flagged (instead of the expected 200).