"""
4.9 Сохраняем результат в JSON
Соберите данные со всех 5 категорий на сайте(https://parsinger.ru/html/index1_page_1.html) тренажере и соберите все данные с карточек.
По результату выполнения кода в папке с проектом должен появится файл .json с отступом в 4 пробела
"""

import json
import requests
from bs4 import BeautifulSoup


# готовит суп
def make_soup(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'lxml')


# получает ссылки на первые страницы категорий товаров
def get_categories():
    soup = make_soup(START_PAGE)
    return [(BASE_URL + x['href']) for x in soup.find('div', class_='nav_menu').find_all('a')]


# получает номер последней страницы из пагинации
def get_cat_last_page(soup):
    return int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])


# получает данные о товарах со страниц категории
def get_data(soup):
    prod_data = []
    names = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    descr_raw = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    descriptions = [[(x.split(':')) for x in y if len(x) > 0] for y in descr_raw]
    prices = [int(x.text.split()[0]) for x in soup.find_all('p', class_='price')]

    # формирует словарь с информацией с карточки товара
    for name, desc, pr in zip(names, descriptions, prices):
        prod_data.append({
            'Наименование': name,
            str(desc[0][0]): desc[0][1].strip(),
            str(desc[1][0]): desc[1][1].strip(),
            str(desc[2][0]): desc[2][1].strip(),
            str(desc[3][0]): desc[3][1].strip(),
            'Цена, руб.': pr
        })
    return prod_data


# сохраняет данные в json-файл
def dump_to_json(js):
    with open('result.json', 'w', encoding='utf-8-sig') as file:
        json.dump(js, file, indent=4, ensure_ascii=False)
    print('Данные сохранены в result.json')
    return True


START_PAGE = 'https://parsinger.ru/html/index1_page_1.html'
BASE_URL = 'https://parsinger.ru/html/'
res_json = []


if __name__ == '__main__':
    for category_page in get_categories():
        soup = make_soup(category_page)
        for current_pagin_page in range(1, get_cat_last_page(soup) + 1):
            url = category_page.split('_page')[0]
            soup = make_soup(f'{url}_page_{current_pagin_page}.html')
            res_json.extend(get_data(soup))

    dump_to_json(res_json)
