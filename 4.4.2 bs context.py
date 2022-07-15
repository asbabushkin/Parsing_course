from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/headphones/5/5_32.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# class search
p = soup.find('p', class_='article').text
# id search
id_ = soup.find('p', id='p_header').text
# attribute search
atr_ = soup.find('span', {'name': 'count'}).text


print(p)
print(id_)
print(atr_)
