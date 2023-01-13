
from bs4 import BeautifulSoup
import requests
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.flipkart.com/bose-new-smart-soundbar-900-dolby-atmos-alexa-built-in-bluetooth-connectivity-google-assistant-speaker/p/itm6d81fcf6751c1?pid=ACCGCXGGKC5GZYXR&lid=LSTACCGCXGGKC5GZYXRBB2PHK&marketplace=FLIPKART&q=alexa&store=search.flipkart.com&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=f781d89c-1854-4ca7-a989-3a8e8f5f3f84.ACCGCXGGKC5GZYXR.SEARCH&ppt=sp&ppn=sp&ssid=odrrs1wii80000001673647881169&qH=277f2a7ecb7cfcd2'

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')

for item in soup.select('[data-id]'):
	try:
		print('----------------------------------------')


		#print(item)
		print(item.select('a img')[0]['alt'])
		print(item.select('a')[0]['href'])

		print(item.select('[id*=productRating]')[0].get_text().strip())
		prices = item.find_all(text=re.compile('₹')) 
		print(prices[0])

		discounts = item.find_all(text=re.compile('off')) 
		print(discounts[0])



	except Exception as e:
		#raise e
		b=0

import datetime
download_date = datetime.date.today()
print(download_date)

import csv

header = ['Produkt', 'Cena', 'Rating', 'Marka', 'Date']
data = ["title_string", "price", "rating", "review_count", "download_date"]

with open('AmazonAlexa.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
