"""
    Откройте сайт http://parsinger.ru/task/1/
    На нём есть 500 ссылок  и только 1 вернёт статус код 200
    Напишите код который поможет найти правильную ссылку
    По этой ссылке лежит секретный код, который необходимо вставить в поле ответа.

"""


import requests

for i in range(1, 500):
    response = requests.get(f'https://parsinger.ru/task/1/{i}.html')

    if response.status_code == 200:
        print(f'{i}.html - {response.status_code}')
