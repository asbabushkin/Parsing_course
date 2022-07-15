"""
5.6 Скроллинг страниц
    Откройте сайт с помощью Selenium http://parsinger.ru/infiniti_scroll_3/
    На сайте есть 5 окошек с подгружаемыми элементами, в каждом по 100 элементов;
    Необходимо прокрутить все окна в самый низ;
    Цель: получить все значение в каждом из окошек и сложить их;
    Получившийся результат вставить в поле ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

nums = []

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/infiniti_scroll_3/')
    tags = browser.find_element(By.CLASS_NAME, 'main').find_elements(By.XPATH, ".//*")
    divs = filter(lambda t: 'scroll-container_' in t.get_attribute(name='id'), tags)
    for d in divs:
        scroll_origin = ScrollOrigin.from_element(d)
        flag = False
        while not flag:
            action = ActionChains(browser)
            action.scroll_from_origin(scroll_origin, delta_x=0, delta_y=3000)
            action.perform()
            if len(browser.find_element(By.ID, d.get_dom_attribute(name='class')).find_elements(By.CLASS_NAME, 'last-of-list')) > 0:
                flag = True
        nums.extend([int(x.text) for x in browser.find_element(By.ID, d.get_dom_attribute(name='class')).find_elements(By.TAG_NAME, 'span')])
    print(sum(nums))
