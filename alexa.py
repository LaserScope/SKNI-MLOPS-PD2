from bs4 import BeautifulSoup
import requests
import time
import datetime

URL = 'https://www.amazon.pl/zupelnie-nowe-echo-dot-4-generacji-wersja-miedzynarodowa/dp/B085K45C3S/ref=lp_22832478031_1_3'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "lxml")



brand = soup.find(id='bylineInfo')


print(brand.text)

import datetime
download_date = datetime.date.today()
print(download_date)

import csv

header = ['Produkt', 'Cena', 'Rating', 'Marka', 'Date']
data = [title, price, rating, brand.text, download_date]

with open('AmazonAlexa.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
