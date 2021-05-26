from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv

URL = 'https://www.otodom.pl/sprzedaz/mieszkanie/slaskie/'

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

def parse_myprice(myprice):
    return float(myprice.replace(' zł','').replace(' ',''))

db = sqlite3.connect('dane.db')
cursor = db.cursor()

for offer in bs.find_all('div', class_='offer-item-details'):
    mytitle = offer.find('span', class_='offer-item-title')
    myprice = offer.find('li', class_='offer-item-price').get_text().strip()
    mylocation = offer.find('p', class_='text-nowrap').get_text().split(': ')[1]
    myrooms = offer.find('li', class_='offer-item-rooms hidden-xs').get_text()
    myarea = offer.find('li', class_='hidden-xs offer-item-area').get_text()
    mypriceperm = offer.find('li', class_='hidden-xs offer-item-price-per-m').get_text()

    print(mylocation,',',myarea,',',myprice)