"""
    Открываем сайт с помощью selenium; https://parsinger.ru/selenium/7/7.html
    Получаем значения всех элементов выпадающего списка;
    Суммируем(плюсуем) все значения;
    Вставляем получившийся результат в поле на сайте;
    Нажимаем кнопку и копируем длинное число;
    Вставляем конечный результат в поле ответа.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

summa = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    options = browser.find_elements(By.TAG_NAME, 'option')
    for opt in options:
        summa += int(opt.text)
    browser.find_element(By.ID, 'input_result').send_keys(summa)
    browser.find_element(By.ID, 'sendbutton').click()
    print(browser.find_element(By.ID, 'result').text)
   
    sleep(5)