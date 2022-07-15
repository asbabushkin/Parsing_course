"""
4.5 Пагинация

    Открываем сайт 'http://parsinger.ru/html/index1_page_1.html'
    Проходимся по всем категориям, страницам и карточкам с товарами(всего 160шт)
    Собираем с каждой карточки стоимость товара умножая на количество товара в наличии
    Складываем получившийся результат
    Получившуюся цифру с общей стоимостью всех товаров вставляем в поле ответа.
"""

from time import time
from bs4 import BeautifulSoup
import requests


START_URL = 'http://parsinger.ru/html/index1_page_1.html'
BASE_URL = 'https://parsinger.ru/html/'
prod_links = []
prod_data = []
summa = 0


def get_num_categories(url):
    """
    Возвращает число категорий товаров
    """
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return len([i['href'] for i in soup.find('div', class_='nav_menu').find_all('a')])


def get_pagen(cat_num):
    """
    Возвращает количество страниц пагинации в категории товаров
    """
    response = requests.get(f'http://parsinger.ru/html/index{cat_num}_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    categ_last_page = int([link.text for link in soup.find('div', class_='pagen').find_all('a')][-1])
    return categ_last_page


def get_prod_pages(categ, page):
    """
    Собирает ссылки на страницы товаров
    """
    response = requests.get(f'http://parsinger.ru/html/index{categ}_page_{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    prod_links.extend([link['href'] for link in soup.find_all('a', class_='name_item')])

    with open('product_links.txt', 'w') as file:
        for link in prod_links:
            file.write(BASE_URL + link + '\n')

    return prod_links


def get_prod_data(product_link):
    """
    Собирает данные о товаре в словарь
    """
    response = requests.get(BASE_URL + product_link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find('p', id='p_header').text
    price = int(soup.find('span', id='price').text[:-4])
    quantity = int(soup.find('span', id='in_stock').text.split()[-1])
    prod_dict = {'name': name, 'price': price, 'quantity': quantity, 'link': BASE_URL + product}
    return prod_dict


if __name__ == '__main__':
    for categ in range(1, get_num_categories(START_URL) + 1):
        last_page = get_pagen(categ)
        for page in range(1, last_page + 1):
            get_prod_pages(categ, page)

    start = time()
    for product in prod_links:
        prod_data.append(get_prod_data(product))
    end = time()
    print(end - start)

    for i in range(len(prod_data)):
        summa += prod_data[i]['price'] * prod_data[i]['quantity']

    print(summa)
