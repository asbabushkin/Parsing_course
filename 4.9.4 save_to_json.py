import json
import requests
from bs4 import BeautifulSoup

# готовит суп
def make_soup(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return BeautifulSoup(resp.text, 'lxml')

# получает номер последней страницы из пагинации
def get_cat_last_page(soup):
    return int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])

# получает данные о товаре со страниц категории
def get_data(soup):
    prod_data = []
    names = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    descr_raw = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    descriptions = [[x.split(':')[1].strip() for x in y if len(x) > 0] for y in descr_raw]
    prices = [int(x.text.split()[0]) for x in soup.find_all('p', class_='price')]

    for name, desc, pr in zip(names, descriptions, prices):
        prod_data.append({
            'name': name,
            'brand': desc[0],
            'type': desc[1],
            'frame_material': desc[2],
            'screen_technology': desc[3],
            'price': pr
        })
    return prod_data

# сохраняет данные в json-файл
def dump_to_json(js):
    with open('result.json', 'w', encoding='utf-8-sig') as file:
        json.dump(js, file, indent=4, ensure_ascii=False)
    print('Данные сохранены в result.json')
    return True


START_PAGE = 'https://parsinger.ru/html/index1_page_1.html'
res_json = []

soup = make_soup(START_PAGE)
for page in range(1, get_cat_last_page(soup) + 1):
    soup = make_soup(f'https://parsinger.ru/html/index1_page_{page}.html')
    res_json.extend(get_data(soup))

dump_to_json(res_json)
