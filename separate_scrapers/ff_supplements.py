import requests
from bs4 import BeautifulSoup


url = 'https://ffsupplements.com.ph/collections/whey-protein'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

products = soup.find_all('div', class_='product-item__info-inner')

for product in products:
    product_name = product.a.text
    price = product.find('span', class_='price').text
    print(f'{product_name} ({price})')

