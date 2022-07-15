from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
# извлекаем все ссылки пагинации и получаем текст, содержащийся в последнем элементе списка.
# Это и есть количество страниц пагиации.
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

print(pagen)