"""
5.4 Поиск элементов Selenium

    Откройте сайт; http://parsinger.ru/selenium/3/3.html
    Извлеките данные из каждого тега <p>;
    Сложите все значения, их всего 300 шт;
    Напишите получившийся результат в поле ниже.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

summa = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    p_list = browser.find_elements(By.TAG_NAME, 'p')
    for p in p_list:
        summa += int(p.text)

print(summa)