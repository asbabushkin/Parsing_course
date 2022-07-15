"""
5.5 Методы Selenium

    Откройте сайт с помощью Selenium; https://parsinger.ru/methods/5/index.html
    На сайте есть 42 ссылки, у каждого сайта по ссылке есть cookie с определёнными сроком жизни;
    Цель: написать скрипт, который сможет найти среди всех ссылок страницу с самым длинным
    сроком жизни cookie и получить с этой страницы число;
    Вставить число в поле для ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

exp_max = 0
link_exp_max = ''

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('https://parsinger.ru/methods/5/index.html')
    pages = [x.get_attribute('href') for x in browser.find_elements(By.TAG_NAME, 'a')]
    for p in pages:
        browser.get(p)
        expiry = int(browser.get_cookie('expiry')['expiry'])
        if expiry > exp_max:
            exp_max = expiry
            link_exp_max = p

    browser.get(link_exp_max)
    print(browser.find_element(By.ID, 'result').text)
