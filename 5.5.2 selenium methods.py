"""

5.5 Методы Selenium

    Откройте сайт с помощью Selenium; https://parsinger.ru/methods/1/index.html
    При обновлении сайта, в id="result" появится число;
    Обновить страницу возможно придется много раз, т.к. число появляется не часто;
    Вставьте полученный результат в поле для овтета:

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    for i in range(200):
        browser.refresh()
        label = browser.find_element(By.ID, 'result').text
        if label != 'refresh page':
            print(label)
            print(i)
            sleep(5)
            break
