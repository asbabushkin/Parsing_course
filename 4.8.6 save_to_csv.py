"""
4.8 Сохраняем результат в Excel

Напишите код, который собирает данные в категории watch (http://parsinger.ru/html/index1_page_1.html)
c каждой карточки, всего их 32.
Информация которую необходимо собрать: Наименование, Артикул, Бренд, Модель, Тип,
Технология экрана, Материал корпуса, Материал браслета, Размер, Сайт производителя,
Наличие, Цена, Старая цена,  Ссылка на карточку с товаром.

Всего должно быть 14 заголовков
"""


import csv
import requests
from bs4 import BeautifulSoup


# принимает ссылку на веб-страницу, возвращает суп
def make_soup(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'lxml')


# находит последнюю страницу категории в пагинации
def get_cat_last_page(soup):
    return int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])


# собирает ссылки на страницы товаров с страницы категории
def get_prod_links(soup):
    return [prod['href'] for prod in soup.find_all('a', class_='name_item')]


# собирает данные о товаре со страницы товара
def get_prod_data(soup, link):
    name = soup.find('p', id='p_header').text
    article = soup.find('p', class_='article').text.split(':')[1].strip()
    params = [i.text.split(':')[1].strip() for i in soup.find('ul', id='description').find_all('li')]
    in_stock = soup.find('span', id='in_stock').text.split(':')[1].strip()
    price = soup.find('span', id='price').text
    old_price = soup.find('span', id='old_price').text
    return [name, article, *params, in_stock, price, old_price, BASE_URL + link]


# записывает данные в файл
def write_csv(headers, data):
    with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
        writer.writerows(data)
    return 'Файл result.csv создан!'


BASE_URL = 'https://parsinger.ru/html/'
first_page = 'http://parsinger.ru/html/index1_page_1.html'
prod_links = []
result = []
headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
           'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя',
           'Наличие', 'Цена', 'Старая цена', 'Ссылка']

soup = make_soup(first_page)
last_page = get_cat_last_page(soup)
for page in range(1, last_page + 1):
    soup = make_soup(f'http://parsinger.ru/html/index1_page_{page}.html')
    prod_links.extend(get_prod_links(soup))

for link in prod_links:
    soup = make_soup(BASE_URL + link)
    result.append(get_prod_data(soup, link))

print(write_csv(headers, result))
