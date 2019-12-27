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

if not os.path.isfile("ranking.html"):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
	url_raking='https://braacket.com/league/hqbwu3/ranking/A5358812-4E18-4CF2-B521-6A194713389A?rows=200'
	req = Request(url=url_raking, headers=headers) 
	html_doc = urlopen(req).read().decode('utf-8')

	file = open("ranking.html",'w')
	file.write(html_doc)

f = open("ranking.html",'r')
html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

dictionary = {}
counter = 1
rows = soup.find_all('tr')
for row in rows:
	tag = row.find('a')
	if tag!=None and not ('\t' in tag.text or '\n' in tag.text or tag.text==""):
		nombre = tag.text
		#print(nombre)
		spans = row.find_all('span',{'class': 'game_characters'})
		personajes = []
		for span in spans:
			images = span.find_all('img', {'class':'game_character game_character-ssbm'})
			for image in images:
				ini, fin = re.search("\/[A-Za-z]*\.",image['src']).span()
				personaje = image['src'][ini+1:fin-1]
				personajes.append(personaje)

		
		dictionary[nombre] = {
			'Ranking': counter,
			'Personajes': personajes
		}
		counter+=1
				
print(dictionary)
with open('ranking.json', 'w') as json_file:
  json.dump(dictionary, json_file)