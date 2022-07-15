"""
5.5 Методы Selenium

    Откройте сайт с помощью Selenium; https://parsinger.ru/methods/3/index.html
    На сайте есть определённое количество секретных cookie;
    Ваша задача получить все значения и суммировать их;
    Полученный результат вставить в поле для ответа.
"""
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    summa = sum([int(c['value']) for c in cookies if 'secret_cookie' in c['name']])

print('summa', summa)


