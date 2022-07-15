from bs4 import BeautifulSoup
import requests
import csv


def soup(url):
    r = requests.get(url, timeout=None)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def get_list_of_text(tags):
    result = []
    for i in tags:
        result.append(i.text.split(':')[-1])
    return result


def links(soup):
    for div in soup.find_all('div', 'sale_button'):
        url = 'http://parsinger.ru/html/' + div.find('a')['href']
        r = requests.get(url, timeout=None)
        r.encoding = 'utf-8'
        card = BeautifulSoup(r.text, 'lxml')
        yield url, card


with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд',
                     'Модель', 'Наличие', 'Цена',
                     'Старая цена', 'Ссылка на карточку с товаром'])

    for j in range(1, 6):
        for i in range(1, 5):
            url = f'http://parsinger.ru/html/index{j}_page_{i}.html'
            page = soup(url)

            for url, link in links(page):
                name = link.find('p', id='p_header').text
                article = link.find('p', 'article').text.split()[-1]
                brand, model, *trush = get_list_of_text(link.find_all('li'))
                amount = link.find('span', id='in_stock').text.split(':')[-1]
                price = link.find('span', id='price').text
                old_price = link.find('span', id='old_price').text
                writer.writerow([name, article, brand, model, amount, price, old_price, url])