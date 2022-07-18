"""5.7 Окна и вкладки
    Откройте сайт с помощью selenium; http://parsinger.ru/window_size/1/
    Необходимо открыть окно таким размером, чтобы рабочая область страницы составляла 555px на 555px;
    Учитывайте размеры границ браузера;
    Результат появится в id="result";
    Вставьте полученный результат в поле для ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep




with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/window_size/1/')
 #   browser.set_window_size(width=555, height=675)
    browser.set_window_size(width=555+12, height=555+128)
    print(browser.find_element(By.ID, 'result').text)
    sleep(3)




