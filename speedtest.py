import requests
from time import time
from bs4 import BeautifulSoup


PROD_DATA = []
prod_links = []
parsers = ['html.parser', 'lxml', 'xml', 'html5lib']


def get_product_data(link, parser):
    response = requests.get(link[:-1], headers={'Cache-Control': 'no-cache'})
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, parser)
    name = soup.find('p', id='p_header').text
    price = int(soup.find('span', id='price').text[:-4])
    quantity = int(soup.find('span', id='in_stock').text.split()[-1])
    prod_dict = {'name': name, 'price': price, 'quantity': quantity, 'link': link}
    PROD_DATA.append(prod_dict)
    return PROD_DATA

if __name__=='__main__':
    # with open('product_links.txt', 'r') as file:
    #     for p in parsers:
    #         for i in range(3):
    #             start = time()
    #             for link in file.readlines():
    #                 get_product_data(link, p)
    #             end = time()
    #             print(f'Парсер: {p} проход: {i} время: {end - start}')
    #             print(len(PROD_DATA))

    with open('product_links.txt', 'r') as file:
        start = time()
        for link in file.readlines():
            response = requests.get(link[:-1])
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html5lib')
            name = soup.find('p', id='p_header').text
            price = int(soup.find('span', id='price').text[:-4])
            quantity = int(soup.find('span', id='in_stock').text.split()[-1])
            prod_dict = {'name': name, 'price': price, 'quantity': quantity, 'link': link}
            PROD_DATA.append(prod_dict)
        end = time()
        print(len(PROD_DATA))
        print(f'Time: {end - start}')