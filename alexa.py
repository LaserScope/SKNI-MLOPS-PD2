import bs4
from bs4 import BeautifulSoup
import requests
import time
import datetime

link = 'https://www.flipkart.com/bose-new-smart-soundbar-900-dolby-atmos-alexa-built-in-bluetooth-connectivity-google-assistant-speaker/p/itm6d81fcf6751c1?pid=ACCGCXGGKC5GZYXR&lid=LSTACCGCXGGKC5GZYXRBB2PHK&marketplace=FLIPKART&q=alexa&store=search.flipkart.com&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=f781d89c-1854-4ca7-a989-3a8e8f5f3f84.ACCGCXGGKC5GZYXR.SEARCH&ppt=sp&ppn=sp&ssid=odrrs1wii80000001673647881169&qH=277f2a7ecb7cfcd2'
page = requests.get(link)
page.content

soup = bs4(page.content, 'html.parser')
print(soup.prettify())

name=soup.find('span',class_="B_NuCI")
print(name)
name.text

price=soup.find('div',class_="_30jeq3 _16Jk6d")
print(price)
price.text

rating=soup.find('span',class_="_2dMYsv")
print(rating)
rating.text

offers=soup.find('div',class_="_1AtVbE col-12-12")
print(offers)
offers.text

specification=soup.find('div',class_="fMghEO")
print(specification)
specification.text

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
