import csv
import requests
from bs4 import BeautifulSoup

# 1 ------------------------------------------------------
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
url = 'http://parsinger.ru/html/index3_page_2.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
price = [x.text for x in soup.find_all('p', class_='price')]
# 3 ------------------------------------------------------

# 4------------------------------------------------------
for item, price, descr in zip(name, price, description):
    result = []
    flatten = item, price, [x.split(':')[1].strip() for x in descr if x]

    # 5 ------------------------------------------------------
    for x in flatten:
        if isinstance(x, list):
            for i in x:
                result.append(i)
        else:
            result.append(x)
    print(result)
    # 5 ------------------------------------------------------

    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(result)
print('Файл res.csv создан')
# 4 ------------------------------------------------------