import requests
from bs4 import BeautifulSoup


url = 'https://www.supplementhub.com.ph/product-category/whey-protein/?orderby=price-desc'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

products = soup.find_all('div', class_='text-center product-details')

for product in products:
    product_name = product.p.a.text
    if product.find('ins') is not None:
        price = product.find('ins').text
    else:
        price = product.find('span', class_='price').text 
    print(f'{product_name} ({price})')
