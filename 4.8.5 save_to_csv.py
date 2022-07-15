"""
4.8 Сохраняем результат в Excel
Напишите код, который собирает данные со всех страниц и категорий
на сайте тренажере(http://parsinger.ru/html/index1_page_1.html) и сохраните всё в таблицу.
Заголовки указывать не нужно.
"""

import csv
import requests
from bs4 import BeautifulSoup

result = []

# делаем запрос к главной веб-странице и достаем из супа количество категорий товаров
response = requests.get(url='http://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
cat_num = len([cat['href'] for cat in soup.find('div', class_='nav_menu').find_all('a')])

# обращаемся к каждой категории и из блока пагинации достаем номер последней страницы категории
for cat in range(1, cat_num+1):
    response = requests.get(f'http://parsinger.ru/html/index{cat}_page_1.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    last_page = int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])

#обращаемся к каждой странице товаров из категории и достаем из супа название, цену и
# характеристики(в виде "сырой" строки) товаров
    for page in range(1, last_page + 1):
        response = requests.get(f'http://parsinger.ru/html/index{cat}_page_{page}.html')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        names = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        prices = [x.text for x in soup.find_all('p', class_='price')]
        descr_raw = [x.text.split('\n') for x in soup.find_all('div', class_='description')]

        # из "сырых" характеристик достаем нужные данные
        descr_new = [[j.split(':')[1].strip() for j in i if len(j) > 0] for i in descr_raw]

        # создаем список с названием, ценой и характеристиками каждого товара и добавляем его
        # в итоговый список result
        for item, price, descr in zip(names, prices, descr_new):
            result.append([item, *descr, price])

# создаем CSV-файл и записываем в него данные из итогового списка
with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(result)

print('Файл result.csv создан')
