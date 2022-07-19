"""
5.8 Ожидания явные и неявные

А это задача для тех кто всё таки решил перехитрить прошлую задачу и решил её вручную.
А для всех остальных, задача максимально проста, запустить тот же самый код из прошлой задачи,
но на другом url и с другим class.

    Откройте сайт при помощи Selenium; http://parsinger.ru/expectations/6/index.html
    На сайте есть кнопка, поведение которой вам знакомо;
    После нажатия на кнопку, на странице начнётся создание элементов class с рандомными значениями;
    Ваша задача применить метод, чтобы он вернул содержимое элемента с классом "Y1DM2GR",
    когда он появится на странице;
    Полученное значение вставить в поле для ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn'))).click()
    if WebDriverWait(browser, 100, poll_frequency=0.2).until(EC.presence_of_element_located((By.CLASS_NAME, 'Y1DM2GR'))):
        print(browser.find_element(By.CLASS_NAME, 'Y1DM2GR').text)
        browser.quit()
