"""
5.6 Скроллинг страниц
    Откройте сайт с помощью Selenium; https://parsinger.ru/infiniti_scroll_1/
    На сайте есть список из 100 элементов, которые генерируются при скроллинге;
    В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
        Используйте Keys.DOWN или .move_to_element();
    Цель: получить все значение в элементах, сложить их;
    Получившийся результат вставить в поле ответа.

Подсказка:
Элементы могут грузится медленнее чем работает ваш код, установите задержки.
Подумайте над условием прерывания цикла, последний элемент в списке имеет class="last-of-list"
"""

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

summa = 0

with webdriver.Chrome() as browser:
    list_input = []
    flag = True
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    while flag:
        check_tags = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]
        span_tags = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]
        tags = zip(check_tags, span_tags)

        for check, span in tags:
            if check not in list_input:
                check.send_keys(Keys.TAB)
                try:
                    check.click()
                    WebDriverWait(webdriver, 3).until(EC.element_to_be_selected(check))
                except TimeoutException:
                    check.click()
                    WebDriverWait(webdriver, 3).until(EC.element_to_be_selected(check))
                finally:
                    summa += int(span.text)
                    list_input.append(check)
                    if span.get_attribute('class') == 'last-of-list':
                        flag = False
print('Summa:', summa)
