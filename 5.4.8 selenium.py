"""
5.4 Поиск элементов Selenium
Вторая задачка тоже довольна проста. Вспоминаем метод By.PARTIAL_LINK_TEXT или
By.LINK_TEXT, который ищет ссылку по частичному или полному совпадению текста.

Суть задачи.
    Открываем сайт при помощи selenium; http://parsinger.ru/selenium/2/2.html
    Применяем метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT;
    Кликаем по ссылке с текстом 16243162441624;
    Результат будет ждать вас в теге <p id="result"></p>  ;
    Скопируйте найденный результат в поле ниже.

p.s. Вы конечно можете вручную найти ссылку, при помощи простого поиска, но кого вы обманете?
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/2/2.html')
    browser.find_element(By.LINK_TEXT, '16243162441624').click()
    sleep(10)