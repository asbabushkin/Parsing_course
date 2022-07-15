"""
Задача:
    Откройте сайт с помощью Selenium; https://parsinger.ru/scroll/4/index.html
    На сайте есть 50 кнопок, которые визуально перекрыты блоками;
    После нажатия на кнопку в id="result" появляется уникальное для каждой кнопки число;
    Цель: написать скрипт который нажимает поочерёдно все кнопки и собирает уникальные числа;
    Все полученные числа суммировать, и вставить результат в поле для ответа.

"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

summa = 0

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    for x in browser.find_elements(By.CLASS_NAME, 'btn'):
        try:
            x.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            # проскроллит страницу, чтобы элемент стал видимым
            browser.execute_script("return arguments[0].scrollIntoView(true);", x)
            x.click()
        finally:
            summa += int(browser.find_element(By.ID, 'result').text)

print(summa)

