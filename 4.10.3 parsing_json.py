"""
4.10 Парсим JSON

Используйте полученный по ссылке JSON чтоб посчитать количество товара в каждой категории.
На вход ожидается словарь. {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
где N это общее количество товаров.

Количество вы найдёте в каждой карточке товара

"""

import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'
response = requests.get(url).json()

cats = {}
for prod in response:
    if prod['categories'] not in cats:
        cats[prod['categories']] = int(prod['count'])
    else:
        cats[prod['categories']] += int(prod['count'])

print(cats)
