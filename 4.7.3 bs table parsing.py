"""
4.7 Парсинг табличных данных
2 из 7 шагов пройдено
7 из 127 баллов  получено

    На  сайте расположена таблица;
    Цель: Собрать числа с 1го столбца и суммировать их;
    Полученный результат вставить в поле ответа.
"""
from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/2/index.html')
soup = BeautifulSoup(response.text, 'lxml')
data = [float(data.text) for data in soup.find('div', class_='main').find_all('td')]
uniq_data = []
[uniq_data.append(i) for i in data if i not in uniq_data]
print(data)
print(uniq_data)
print(sum(uniq_data))
print(round(sum(uniq_data), 3))