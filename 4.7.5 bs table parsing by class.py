"""
4.7 Парсинг табличных данных

    На  сайте расположена таблица https://parsinger.ru/table/4/index.html;
    Цель: Собрать числа в зелёных ячейках и суммировать их;
    Полученный результат вставить в поле ответа.
"""

from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/4/index.html')
soup = BeautifulSoup(response.text, 'lxml')
data = [float(tag.text) for tag in soup.find_all('td', class_='green')]
print(round(sum(data), 3))