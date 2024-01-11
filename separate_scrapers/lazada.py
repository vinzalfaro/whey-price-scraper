import requests
from bs4 import BeautifulSoup


url = 'https://www.lazada.com.ph/tag/whey-protein'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

products = soup.find_all('div', class_='buTCk')

for product in products:
    product_name = product.find('div', class_='RfADt').a.text
    price = product.find('span', class_='ooOxS').text
    print(f'{product_name} ({price})')

