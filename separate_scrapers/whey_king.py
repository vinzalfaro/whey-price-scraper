import requests
from bs4 import BeautifulSoup


url = 'https://www.wheykingsupplements.com/collections/whey-protein'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

products = soup.find_all('div', class_='productitem--info')

for product in products:
    product_name = product.h2.a.text.strip()
    price = product.find('span', class_='money').text.strip()
    print(f'{product_name} ({price})')