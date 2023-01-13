from bs4 import BeautifulSoup
import requests
import time
import datetime

def get_title(soup):
	
	try:
		title = soup.find("span", attrs={'id':'productTitle'})
		title_value = title.string
		title_string = title_value.strip()
	
	except AttributeError:
		title_string = ""
		
	return title_string

def get_price(soup):

	try:
		price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
		
	except AttributeError:
		price = ""

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

	return review_count

if __name__ == '__main__':
	HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
	URL = 'https://www.amazon.pl/fire-tv-stick-wersja-miedzynarodowa-z-pilotem-alexa-voice-remote-urz%C4%85dzenie-do-przesylania-strumieniowego-hd/dp/B098J3NXBZ/ref=lp_20772983031_1_4'
	
	page = requests.get(URL, headers=HEADERS)
	soup = BeautifulSoup(page.content, "lxml")
	
	print("Product Title =", get_title(soup))
	print("Product Price =", get_price(soup))
	print("Product Rating =", get_rating(soup))
	print("Number of Product Reviews =", get_review_count(soup))
	
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
