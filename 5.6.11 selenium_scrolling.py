"""
5.6 Скроллинг страниц

Для скроллинга окна используйте .scroll(0,0,0,0) , где координаты окна которое необходимо скролить.
    Откройте сайт с помощью Selenium; http://parsinger.ru/infiniti_scroll_2/
    На сайте есть список из 100 элементов, которые генерируются при скроллинге;
    Необходимо прокрутить окно в самый низ;
    Цель: получить все значение в элементах, сложить их;
    Получившийся результат вставить в поле ответа.


"""

from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.ID, 'scroll-wrapper')
    scroll_origin = ScrollOrigin.from_element(div)
    flag = False
    action = ActionChains(browser)
    while not flag:
        action.scroll_from_origin(scroll_origin, delta_x=0, delta_y=1000)
        action.perform()
        if len(browser.find_element(By.ID, 'scroll-container').find_elements(By.CLASS_NAME, 'last-of-list')) > 0:
            flag = True

    print(sum([int(x.text) for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'p')]))
