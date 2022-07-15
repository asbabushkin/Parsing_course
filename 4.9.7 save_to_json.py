"""
4.9 Сохраняем результат в JSON

Соберите данные со всех 5 категорий на сайте тренажере (https://parsinger.ru/html/watch/1/1_1.html)
 и соберите все данные с карточек. По результату выполнения кода в папке с проектом
 должен появится файл .json с отступом в 4 пробела. Ключи в блоке description должны быть
 получены автоматически из атрибутов HTML элементов.
"""

import json
import requests
from bs4 import BeautifulSoup


# возвращает суп
def make_soup(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'lxml')


# возвращает список ссылок на первые старницы категорий
def get_all_cats():
    soup = make_soup(FIRST_PAGE)
    return [x['href'] for x in soup.find('div', class_='nav_menu').find_all('a')]


# возвращает номер последней страницы из пагинации
def get_cat_last_page(soup):
    return int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])


# возвращает ссылки на страницы товаров
def get_prod_links(soup):
    return [x['href'] for x in soup.find('div', class_='item_card').find_all('a', class_='name_item')]


# возвращает словарь с данные о товаре, взятыми со страницы товара
def get_data(soup):
    return {
        'category': i.split('/')[0],
        'name': soup.find('p', id='p_header').text,
        'article': soup.find('p', class_='article').text.split(':')[1].strip(),
        'in_stock': soup.find('span', id='in_stock').text.split(':')[1].strip(),
        'description': dict(zip([x['id'] for x in soup.find('ul', id='description').find_all('li')],
                                [x.text.split(':')[1].strip() for x in soup.find('ul', id='description').find_all('li')
                                 if len(x) > 0])),
        'price': soup.find('span', id='price').text,
        'old_price': soup.find('span', id='old_price').text,
        'link': BASE_URL + i
    }


# сохраняет данные в json-файл
def dump_to_json(js):
    with open('result.json', 'w', encoding='utf-8-sig') as file:
        json.dump(js, file, indent=4, ensure_ascii=False)
    print('Данные сохранены в result.json')
    return True


FIRST_PAGE = 'https://parsinger.ru/html/index1_page_1.html'
BASE_URL = 'https://parsinger.ru/html/'
json_lst = []

if __name__ == '__main__':
    print('Поехали!')
    for cat in get_all_cats():
        print(f'Обрабатывается категория {cat[5]}')
        soup = make_soup(BASE_URL + cat)
        for page in range(1, get_cat_last_page(soup) + 1):
            soup = make_soup((BASE_URL + cat).split('_page_')[0] + f'_page_{page}.html')
            for i in get_prod_links(soup):
                soup = make_soup(BASE_URL + i)
                json_lst.append(get_data(soup))
    dump_to_json(json_lst)
    print('Готово!')
