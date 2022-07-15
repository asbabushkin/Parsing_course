"""
5.4 Поиск элементов Selenium

Самое время выполнить простую задачку для закрепления пройденного материала.
Суть задачи проста( у вас будет всего 5 секунд для того чтобы получить результат,
поэтому подумайте над кодом)

    Открыть сайт с помощью selenium;
    Заполнить все существующие поля;
    Нажмите на кнопку;
    Скопируйте результат который появится рядом с кнопкой в случае если вы уложились в 5 секунд;
    Вставьте результат в поле ниже.

Для заполнения полей вам потребуется метод .send_keys("Текст"), который мы применяем к каждому полю input, помните про универсальный метод .find_elements(), который возвращает список найденных элементов. Используйте этот метод для поиска всех полей.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://stepik-parsing.ru/selenium/1/1.html')
    input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
    time.sleep(5)

Для решения задачи используйте цикл,  чтобы обойти найденные элементы, методом .find_elements(), и на каждой итерации к каждому полю применяйте метод .send_keys("text") для его заполнения, а метод .click() используйте чтобы нажать на кнопку. Не забудьте про модуль time чтобы установить задержки.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

text = ['Ivan', 'Ivanov', 'Ivanovich', 35, 'Moscow', 'ivanov@ya.ru']
with webdriver.Chrome() as browser:
    browser.get('https://stepik-parsing.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'form')
    [input_form[i].send_keys(text[i]) for i in range(len(input_form))]
    browser.find_element(By.ID, 'btn').click()
    time.sleep(5)
