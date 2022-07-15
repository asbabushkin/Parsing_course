"""
4.5 Пагинация

    Открываем сайт http://parsinger.ru/html/index3_page_4.html
    Проходимся по всем страницам в категории мыши (всего  4 страницы)
    На каждой странице посещаем каждую карточку с товаром (всего 32 товаров)
    В каждой карточке извлекаем при помощи bs4 артикул <p class="article"> Артикул: 80244813 </p>
    Складываем(плюсуем) все собранные значения
    Вставляем получившийся результат в поле ответа

"""

from bs4 import BeautifulSoup
import requests

URL = 'http://parsinger.ru/html/index3_page_1.html'
SHEMA = 'http://parsinger.ru/html/'
summa = 0

response = requests.get(url=URL)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# извлекаем все ссылки пагинации и получаем текст, содержащийся в последнем элементе списка.
# Это и есть количество страниц пагиации.
last_page = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

"""
Формируем ссылку для каждой страницы с товарами, проходим по ним циклом, скачивая нужные данные.
"""
links = []
for page in range(1, int(last_page) + 1):
    response = requests.get(f'http://parsinger.ru/html/index3_page_{page}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    links_goods = [SHEMA + i['href'] for i in soup.find_all('a', class_='name_item')]
    links.extend(links_goods)

print(links)
print(len(links))
vendor_codes = []
for i in links:
    response = requests.get(i)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    vendor_code = soup.find('p', class_='article').text[9:]
    vendor_codes.append(int(vendor_code))
print(vendor_codes)
print(sum(vendor_codes))