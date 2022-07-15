"""
4.5 Пагинация

    Откройте сайт http://parsinger.ru/html/index3_page_1.html
    Извлеките названия товара с каждой страницы (всего 4х страниц)
    Данные с каждой страницы должны хранится в списке.
    По итогу работы должны получится 4 списка которые хранятся в списке(список списков)
    Отправьте получившийся список списков в поле ответа.
    Метод strip()использовать не нужно

Пример ожидаемого списка

[[' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N'], [' name1 ', 'name2', ' ... ', ' name_N']]
"""
from bs4 import BeautifulSoup
import requests

URL = 'http://parsinger.ru/html/index3_page_1.html'
SHEMA = 'http://parsinger.ru/html/'


response = requests.get(url=URL)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# извлекаем все ссылки пагинации и получаем текст, содержащийся в последнем элементе списка.
# Это и есть количество страниц пагиации.
last_page = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

"""
Формируем ссылку для каждой страницы с товарами, проходим по ним циклом, скачивая нужные данные.
"""
goods = []
for page in range(1, int(last_page)+1):
    response = requests.get(f'http://parsinger.ru/html/index3_page_{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    page_goods = [i.text for i in soup.find_all('a', class_='name_item')]
    goods.append(page_goods)

print(goods)





