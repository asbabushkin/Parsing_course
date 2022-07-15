"""
4.10 Парсим JSON

Используйте полученный по ссылке JSON чтоб посчитать стоимость товаров в каждой отдельной категории.
На вход ожидается словарь. {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
где N это общая стоимость товаров в категории.
"""

import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'
total_cost = {}

response = requests.get(url).json()
for prod in response:
    if prod['categories'] not in total_cost:
        total_cost[prod['categories']] = int(prod['count']) * int(prod['price'].split()[0])
    else:
        total_cost[prod['categories']] += int(prod['count']) * int(prod['price'].split()[0])

print(total_cost)