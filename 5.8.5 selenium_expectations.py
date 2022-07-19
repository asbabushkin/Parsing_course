"""
5.8 Ожидания явные и неявные

    Откройте сайт при помощи Selenium; http://parsinger.ru/expectations/4/index.html
    На сайте есть кнопка, которая становится активной после загрузки страницы с
    рандомной задержкой, от 1 до 3 сек;
    После нажатия на кнопку, в title начнут появляться коды, с рандомным временем,
    от 0,1 до 0.6 сек;
    В этот раз второй раз на кнопку кликать не нужно, а нужно получить title целиком,
    если часть title ="JK8HQ"
    Используйте метод title_contains(title) с прошлого урока;
    Вставьте полный текст заголовка который совпадает с частью заголовка из условия.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/4/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    if WebDriverWait(browser, 100).until(EC.title_contains('JK8HQ')):
        print(browser.title)