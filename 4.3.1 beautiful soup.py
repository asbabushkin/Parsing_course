from bs4 import BeautifulSoup
import requests
import lxml


"""
Передаём текстовый файл  с разметкой HTML.
Такой вариант используется в основном для написания и отладки наших парсеров. 
Когда сервер очень злой и мы часто улетаем в бан из-за огромного количества запросов к серверу. 
Тогда мы сохраняем весь HTML страницы  в файл и безопасно парсим уже с нашего HDD."""

# # Пример 1. Передача файла HTML напрямую без использования менеджера контекста
# file = open('index.html', encoding='utf-8')
# soup = BeautifulSoup(file, 'lxml')
# print(soup)
#
# # Пример 2. Передача файла HTML напрямую с использованем менеджера контекста
# with open('index.html', 'r', encoding='utf-8') as file:
#     soup2 = BeautifulSoup(file, 'lxml')
#     print(soup2)


"""
Передаём объект response.text
"""
# Пример 3. Передача объекта response прямо из запроса
response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
