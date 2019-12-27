import os 
import sys
import json
import re
from urllib.request import urlopen, Request 
from urllib.error import HTTPError
from datetime import date, timedelta
import unicodedata
from bs4 import BeautifulSoup
import re
from datetime import datetime


if not os.path.isfile("torneo.html"):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
	url_torneo='https://smash.gg/tournament/melee-dm-4/events/melee-singles/brackets/675512/1102945'
	req = Request(url=url_torneo, headers=headers) 
	html_doc = urlopen(req).read().decode('utf-8')

	file = open("torneo.html",'w')
	file.write(html_doc)

f = open("torneo.html",'r')
html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(html_doc)

spans = soup.find_all('div', {'class': 'match-affix-wrapper'})
print(spans)

#'class':'sgg2qW2i'