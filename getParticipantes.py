import os 
import sys
import json
from urllib.request import urlopen, Request 
from urllib.error import HTTPError
from datetime import date, timedelta
import unicodedata
from bs4 import BeautifulSoup
import re
from datetime import datetime

reg_url = "https://smash.gg/tournament/melee-dm-4/attendees"
print(reg_url)

if not os.path.isfile("attendees.html"):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
	req = Request(url=reg_url, headers=headers) 
	html_doc = urlopen(req).read().decode('utf-8')

	file = open("attendees.html",'w')
	file.write(html_doc)
	
f = open("attendees.html",'r')
html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

spans = soup.find_all('span',{'class' : 'sgg2Npqr sgg20NMf'})
nombres = [span.get_text() for span in spans]
print(nombres)
