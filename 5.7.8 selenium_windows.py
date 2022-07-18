"""
5.7 Окна и вкладки
Для этой задачи потребуется код с прошлого степа.
    Откройте сайт с помощью selenium; http://parsinger.ru/window_size/2/index.html
    У вас есть 2 списка с размера окон size_x и size_y;
    Цель: определить размер окна, при котором,  в id="result" появляется число;
    Результат должен быть в виде словаря {'width': size_x, 'height': size_y}

ps. При написании кода, учитывайте размер рамок браузера.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/window_size/2/index.html')
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x, y)
            if len(browser.find_element(By.ID, 'result').text) != 0:
                print(browser.get_window_size())
                break
