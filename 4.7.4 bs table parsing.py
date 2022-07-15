"""
4.7 Парсинг табличных данных

    На  сайте расположена таблица;
    Цель: Собрать числа которые выделены жирным шрифтом и суммировать их;
    Полученный результат вставить в поле ответа.
"""
from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/table/3/index.html')
soup = BeautifulSoup(response.text, 'lxml')

# решение препода
#summa = [float(x.text) for x in soup.find_all('td') if x.find('td') != x.find('b')]


summa = [float(child.text) for tag in soup.find_all('td') for child in tag if child.name == 'b']

# то же самое вложенным циклом
# summa = 0
# for tag in soup.find_all('td'):
#     for child in tag:
#         if child.name == 'b':
#             summa += float(child.text)
    # for j in i.find('b'):
    #     print(j.text)

#print(round(summa, 3))
print(round(sum(summa), 3))