"""
4.7 Парсинг табличных данных

    На  сайте расположена таблица;
    Цель: Собрать все уникальные числа из таблицы и суммировать их;
    Полученный результат вставить в поле ответа.

"""
from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/1/index.html')
soup = BeautifulSoup(response.text, 'lxml')
data = [float(i.find('td').text) for i in soup.find_all('tr')[1:]]

print(sum(data))
