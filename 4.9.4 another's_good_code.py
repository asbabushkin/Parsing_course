# обращаю ваше внимание, что можно парсить любую категорию
from bs4 import BeautifulSoup
import requests, json


def get_site(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    site = BeautifulSoup(response.text, 'lxml')
    return site


print('Научинаю обработку сайта...')
url = 'https://parsinger.ru/html/index1_page_1.html'
all_urls = []
template = 'https://parsinger.ru/html/'
for u in [n['href'] for n in get_site(url).find('div', class_='pagen').find_all('a')]:
    all_urls.append(template + u)
print('Список ссылок сформирован...')
data = []
for u in all_urls:
    page = get_site(u)
    item = page.find_all('div', class_='item')
    print('Найдены все карточки на странице', str(all_urls.index(u) + 1) + '...')
    for i in item:
        li = i.find('div', class_='description').find_all('li')
        li = [l.text.split(':')[1].strip() for l in li]
        print(li)
        data.append({
            'name': i.find('a', class_='name_item').text,
            'brand': li[0],
            'type': li[1],
            'material': li[2],
            'screen': li[3],
            'price': i.find('p', class_='price').text.split()[0]
        })
    print('Cписок словарей из страницы', all_urls.index(u) + 1, 'сформирован...')
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
print('Файл res.json сформирован...')
