"""
4.7 Парсинг табличных данных
    На  сайте расположена таблица https://parsinger.ru/table/5/index.html;
    Цель: Умножить число в оранжевой ячейке на число в голубой ячейке в той же строке и всё суммировать;
    Полученный результат вставить в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'lxml')

orange = [float(cell.text) for cell in soup.find_all('td', class_='orange')]
rows = [[float(cell.text) for cell in row.find_all('td')] for row in soup.find_all('tr')]
# последние ячейки строк можно найти так:
#last = [int(x.find_all('td')[-1].text) for x in soup.find_all('tr') if x.find('td')]
rows.pop(0)
result = 0
if len(rows) == len(orange):
    for i in range(len(orange)):
        result += orange[i] * rows[i][-1]
    print(round(result, 3))
else:
    print('Длина списков не совпадает')


""" 
решение через селекторы

blue_sel = [float(cell.text) for cell in soup.select('td:last-child')]
orange_sel = [float(cell.text) for cell in soup.select('.orange')]
result = 0
if len(blue_sel) == len(orange_sel):
    for i in range(len(orange_sel)):
        result += orange_sel[i] * blue_sel[i]
    print(round(result, 3))
else:
    print('Длина списков не совпадает')
"""

