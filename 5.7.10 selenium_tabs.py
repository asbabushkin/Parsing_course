""" 5.7 Окна и вкладки

    Откройте сайт с помощью Selenium; http://parsinger.ru/blank/3/index.html
    На сайте есть 10 buttons, каждый button откроет сайт в новой вкладке;
    Каждая вкладка имеет в title уникальное число;
    Цель - собрать числа с каждой вкладки и суммировать их;
    Полученный результат вставить в поле для ответа.
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

summa = 0

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/3/index.html')
    [btn.click() for btn in browser.find_elements(By.CLASS_NAME, 'buttons')]
    sleep(3)
    for i in range(1, len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[i])
        summa += int(browser.execute_script('return document.title;'))
    print(summa)
