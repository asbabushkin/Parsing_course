"""
5.4 Поиск элементов Selenium

    Откройте сайт; http://parsinger.ru/selenium/3/3.html
    Извлеките данные из каждого  второго тега <p>;
    Сложите все значения, их всего 100 шт;
    Напишите получившийся результат в поле ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

summa = 0

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    div_list = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    for div in div_list:
        summa += int(div.text)

print(summa)
