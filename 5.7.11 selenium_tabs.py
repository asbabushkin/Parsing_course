"""
5.7 Окна и вкладки
    У вас есть список сайтов, 6 шт;
    На каждом сайте есть chekbox, нажав на этот chekbox появится код;
    Ваша задача написать скрипт, который открывает при помощи Selenium все сайты во вкладках;
    Проходит в цикле по каждой вкладке, нажимает на chekbox и сохранеят код;
    Из каждого числа, необходимо извлечь корень, функцией sqrt();
    Суммировать получившиеся корни и вставить результат в поле для ответа.

ps. Верный ответ содержит  9 знаков после запятой, т.е имеет вид 000000.000000000

psps. Рекомендую не пытаться обманывать, и извлекать числа другими способами. Работа с вкладками
это одна из важных тем, которую необходимо освоить.
"""

from math import sqrt
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html']
summa = 0

with webdriver.Chrome() as browser:
    browser.get(sites[0])
    [browser.execute_script(f'window.open("{s}");') for s in sites[1:]]
    for tab in browser.window_handles:
        browser.switch_to.window(tab)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()
        summa += sqrt(int(browser.find_element(By.ID, 'result').text))

    print(round(summa, 9))
    sleep(5)
