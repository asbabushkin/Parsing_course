import requests
from bs4 import BeautifulSoup
import csv

def head_csv(name, head,):
    with open(name, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(head)

def row_csv(file_name, res,):
    with open(file_name, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(res)

def get_soup(url):
    response = requests.get(url=url)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

url = "https://parsinger.ru/html/index4_page_1.html"
site = "https://parsinger.ru/html/"
file_name = 'res.csv'
headers = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объём буф. памяти', 'Цена',]
head_csv(file_name, headers)

soup = get_soup(url)
pagen = [f"{site}{i['href']}" for i in soup.find('div', class_='pagen').find_all('a')]
for i in pagen:
    soup = get_soup(i)
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    #test = soup.find_all('div', class_='description')

    price = [x.text for x in soup.find_all('p', class_='price')]
    for item, price, descr in zip(name, price, description):
        result = []
        flatten = item, [x.split(':')[1].strip() for x in descr if x], price
        for x in flatten:
            if isinstance(x, list):
                result.extend(x)
            else:
                result.append(x)
        row_csv(file_name, result)