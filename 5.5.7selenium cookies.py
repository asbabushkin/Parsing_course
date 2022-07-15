"""
5 Методы Selenium
    Откройте сайт с помощью Selenium; https://parsinger.ru/methods/3/index.html
    Ваша задача получить все значения cookie с чётным числом после "_" и суммировать их;
    Полученный результат вставить в поле для ответа.
"""
from selenium import webdriver

summa = 0

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    for c in cookies:
        if 'secret_cookie' in c['name']:
            if int(c['name'].split('_')[2]) % 2 == 0:
                summa += int(c['value'])

    print(summa)







