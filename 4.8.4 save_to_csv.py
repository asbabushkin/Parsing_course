"""
4.8 Сохраняем результат в Excel
Напишите код, который собирает данные в категории HDD(http://parsinger.ru/html/index4_page_1.html)
со всех 4х страниц и сохраняет всё в таблицу по примеру предыдущего степа.
Информация, которую нужно собрать: наименование, Бренд, Форм-фактор, Ёмкость, Объём буф. памяти, Цена
"""

import csv
import requests
from bs4 import BeautifulSoup

result = []

# делаем запрос к веб-странице, готовим суп, достаем из блока пагинации номер последней страницы товаров
response = requests.get(url='http://parsinger.ru/html/index4_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
last_page = int([page.text for page in soup.find('div', class_='pagen').find_all('a')][-1])

# для каждой страницы категории достаем из супа название, цену и характеристики(в виде сырой строки)
# товаров
for page in range(1, last_page + 1):
    response = requests.get(f'http://parsinger.ru/html/index4_page_{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    names = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    prices = [x.text for x in soup.find_all('p', class_='price')]
    descr_raw = [x.text.split('\n') for x in soup.find_all('div', class_='description')]

    # из необработанных характеристик достаем нужные данные
    descr_new = [[j.split(':')[1].strip() for j in i if len(j) > 0] for i in descr_raw]

    # в итоговый список добавляем список с названием, ценой и характеристиками каждого товара
    for item, price, descr in zip(names, prices, descr_new):
        result.append([item, price, *descr])

# создаем CSV-файл и записываем в него полученные данные.
with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Цена', 'Бренд', 'Форм-фактор', 'Емкость', 'Объем буф. памяти'])
    writer.writerows(result)
print('Файл result.csv создан')
