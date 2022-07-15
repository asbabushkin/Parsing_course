"""
4.4 Поиск узлов и элементов

    Открываем сайт https://parsinger.ru/html/hdd/4/4_1.html
    Получаем данные при помощи bs4 о старой цене и новой цене
    По формуле высчитываем процент скидки
    Формула (старая цена - новая цена) * 100 / старая цена)
    Вставьте получившийся результат в поле ответа
    Ответ должен быть числом с 1 знаком после запятой.
"""
from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/html/hdd/4/4_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
price = int(soup.find('span', id='price').text[:-4])
old_price = int(soup.find('span', id='old_price').text[:-4])
print(price, old_price)
discount = round((old_price-price)*100/old_price, 1)
print(discount)
