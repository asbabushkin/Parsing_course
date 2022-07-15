from bs4 import BeautifulSoup
import requests

url = 'http://stepik-parsing.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
#find tags li in div class=item
div = soup.find('div', class_='item').find_all('li')
print(div)
print(type(div))

#print contents of the list
for d in div:
    print(d.text)