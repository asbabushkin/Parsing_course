"""
4.8 Сохраняем результат в Excel
Напишите код, который собирает данные в каждой категории c каждой
карточки(http://parsinger.ru/html/index1_page_1.html), всего их 160.
Информация которую необходимо собрать: Наименование, Артикул, Бренд, Модель, Наличие, Цена,
Старая цена, Ссылка на карточку с товаром,
Перечисленные заголовки являются общими для всех карточек.
"""

import csv
import requests
from bs4 import BeautifulSoup


# готовит суп
def make_soup(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'lxml')


# возвращает список со ссылками на первые страницы категорий
def get_cat():
    soup = make_soup(FIRST_PAGE)
    return [i['href'].split('_page')[0] for i in soup.find('div', class_='nav_menu').find_all('a')]


# находит последнюю страницу категории в пагинации
def get_cat_last_page(soup):
    return int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])


# собирает ссылки на страницы товаров со страницы категории
def get_prod_links(soup):
    return [prod['href'] for prod in soup.find_all('a', class_='name_item')]


# собирает данные о товаре со страницы товара
def get_prod_data(soup, link):
    name = soup.find('p', id='p_header').text
    article = soup.find('p', class_='article').text.split(':')[1].strip()
    brand = soup.find('li', id='brand').text.split(':')[1].strip()
    model = soup.find('li', id='model').text.split(':')[1].strip()
    in_stock = soup.find('span', id='in_stock').text.split(':')[1].strip()
    price = soup.find('span', id='price').text
    old_price = soup.find('span', id='old_price').text
    return [name, article, brand, model, in_stock, price, old_price, BASE_URL + link]


# записывает данные в файл
def write_csv(header, data):
    try:
        with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(header)
            writer.writerows(data)
        return 'Файл result.csv создан!'
    except:
        return 'Ошибка доступа к файлу result.csv'


BASE_URL = 'https://parsinger.ru/html/'
FIRST_PAGE = 'http://parsinger.ru/html/index1_page_1.html'
prod_links = []
result = []
headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка']

if __name__ == '__main__':
    for cat in get_cat():
        soup = make_soup(BASE_URL + cat + '_page_1.html')
        last_page = get_cat_last_page(soup)

        for page in range(1, last_page + 1):
            soup = make_soup(f'http://parsinger.ru/html/{cat}_page_{page}.html')
            prod_links.extend(get_prod_links(soup))

    for pl in prod_links:
        soup = make_soup(BASE_URL + pl)
        result.append(get_prod_data(soup, pl))

    print(write_csv(headers, result))
