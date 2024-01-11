import requests
from bs4 import BeautifulSoup


def request(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def scrape_supplementhub(list):
    url1 = 'https://www.supplementhub.com.ph/product-category/whey-protein/?orderby=price-desc'
    html = request(url1)
    products = html.find_all('div', class_='text-center product-details')

    for product in products:
        product_name = product.p.a.text
        if product.find('ins') is not None:
            price = product.find('ins').text
        else:
            price = product.find('span', class_='price').text
        list.append([product_name, price, 'www.supplementhub.com.ph'])


def scrape_wheyking(list):
    url2 = 'https://www.wheykingsupplements.com/collections/whey-protein'
    html = request(url2)
    products = html.find_all('div', class_='productitem--info')

    for product in products:
        product_name = product.h2.a.text.strip()
        price = product.find('span', class_='money').text.strip()
        list.append([product_name, price, 'www.wheykingsupplements.com'])


def scrape_ffsupplements(list):
    url3 = 'https://ffsupplements.com.ph/collections/whey-protein'
    html = request(url3)
    products = html.find_all('div', class_='product-item__info-inner')

    for product in products:
        product_name = product.a.text
        price = product.find('span', class_='price').text
        list.append([product_name, price, 'ffsupplements.com.ph'])


def write_csv(list, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('"Product","Price","Shop"\n')
        for product in list:
            f.write(f'"{product[0]}","{product[1]}","{product[2]}"\n')


whey_price = []
scrape_supplementhub(whey_price)
scrape_wheyking(whey_price)
scrape_ffsupplements(whey_price)
write_csv(whey_price, 'whey_price.csv')