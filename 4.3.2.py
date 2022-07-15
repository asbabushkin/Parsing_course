"""

4.3 Приготовление супа

    Скачайте по ссылке zip архив при помощи requests http://parsinger.ru/downloads/cooking_soup/index.zip
    Распакуйте архив в папку с вашим проектом
    Извлеките из index.html его содержимое при помощи bs4 и парсера 'lxml'
    Вставьте содержимое в поле ответа


"""

import requests
from bs4 import BeautifulSoup

# response = requests.get('http://parsinger.ru/downloads/cooking_soup/index.zip')
# with open(f'/media/sf_Python/Parsing_course/index.zip', 'wb') as file:
#     file.write(response.content)

file = open('index.html', encoding='utf-8')
soup = BeautifulSoup(file, 'lxml')
print(soup)