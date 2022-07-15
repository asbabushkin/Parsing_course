"""
    Открываем сайт http://parsinger.ru/html/index1_page_1.html
    Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
    Складываем все числа
    Вставляем результат в поле ответа

"""
from bs4 import BeautifulSoup
import requests

response = requests.get(url='http://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
prices = [int(p.text[:-4]) for p in soup.find_all('p', class_='price')]
print(prices)
print(sum(prices))
