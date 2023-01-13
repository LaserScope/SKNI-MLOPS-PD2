from bs4 import BeautifulSoup
import requests
import time
import datetime

URL = 'https://www.amazon.pl/zupelnie-nowe-echo-dot-4-generacji-wersja-miedzynarodowa/dp/B085K45C3S/ref=lp_22832478031_1_3'
headers = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "lxml")

def get_title(soup):
	
	try:
		title = soup.find("span", attrs={"id":'productTitle'})
		title_value = title.string
		title_string = title_value.strip()
	except AttributeError:
		title_string = ""
	print(title_string)

	return title_string

def get_price(soup):

	try:
		price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

	except AttributeError:
		price = ""
	print(price)

	return price

def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""
		print(rating)

	return rating

def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""
	print(review_count)

	return review_count


import datetime
download_date = datetime.date.today()
print(download_date)

import csv

header = ['Produkt', 'Cena', 'Rating', 'Marka', 'Date']
data = [title_string, price, rating, review_count, download_date]

with open('AmazonAlexa.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
