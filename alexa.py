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

title = soup.find("span", attrs={"id":'productTitle'})
title_value = title.string
title_string = title_value.strip()
print(title_string)

price = soup.find("span", attrs={"class":'a-offscreen'})
price_value = price.string
print(price_value)

rating = soup.find("span", attrs={"class":'a-icon-alt'})
rating_value = rating.string
print(rating_value)


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
