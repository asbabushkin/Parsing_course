"""
    4.7 Парсинг табличных данных

    На  сайте расположена таблица https://parsinger.ru/table/5/index.html
    Цель: Написать скрипт который формирует словарь, где ключ будет автоматически формироваться из заголовка таблицы,
    а значения это сумма всех чисел в столбце;
    Полученный словарь вставить в поле ответа.

ps. Округлить каждое число в значении до 3х символов после запятой.

Пример ожидаемого словаря:
{'1 column': 000.000, '2 column': 000.000, '3 column': 000.000, '4 column': 000.000, '5 column':
000.00, '6 column': 000.000, '7 column': 000.000, '8 column': 000.000, '9 column': 000.000,
'10 column': 000.000, '11 column': 000.000, '12 column': 000.000, '13 column': 000.000, '14 column':
000.000, '15 column': 000000.0}
"""
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')
keys = [cell.text for cell in soup.find_all('th')]
data = [[float(cell.text) for cell in row.find_all('td')] for row in soup.find_all('tr') if row.find('td')]
data = list(zip(*data))
values = [round(sum(i), 3) for i in data]
result = {key: value for key, value in zip(keys, values)}
print(result)
