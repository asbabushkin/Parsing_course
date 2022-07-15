"""
download pictures from caseplace.ru
"""
from bs4 import BeautifulSoup
import requests

response = requests.get('https://case-place.ru/chehly-dlya-xiaomi/chehly-dlya-xiaomi-mi-9')
response.encoding = 'windows-1251'
soup = BeautifulSoup(response.text, 'lxml')
descr = [t.text for t in soup.find_all('span', class_='col-12 box-item--case-name px-2')]
pic_links = soup.find_all('meta', itemprop="contentUrl")

print(descr)
print(pic_links)
links = []
for p in pic_links:

    p=str(p)
    p = p[15:-25]
    links.append(p)

print(links)
print(len(links))

for i in range(1, len(links)+1):
    response = requests.get(links[i])
    with open(f'/media/sf_Python/Parsing_course/images_caseplace/{i}.jpg', 'wb') as file:
        file.write(response.content)