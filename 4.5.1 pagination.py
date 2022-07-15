from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_3.html'
shema = 'http://parsinger.ru/html/'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = soup.find('div', class_='pagen').find_all('a')

print(pagen)
list_link = []
for link in pagen:
    list_link.append(link['href'])
"""
Обратите внимание на то как мы получаем значение атрибута href='', подобным образом мы можем 
извлекать ссылку из тегов <a>, такой подход  применим и к тегу <img>, мы сможем извлечь src='',  
напомню что в src='' тега img хранится ссылка на изображения. Картинки мы будем парсить 
в следующих уроках."""
print(list_link)

for i in range(len(list_link)):
    list_link[i] = shema + list_link[i]

print(list_link)