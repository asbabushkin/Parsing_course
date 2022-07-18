"""
5.7 Окна и вкладки
    Откройте сайт с помощью selenium; http://parsinger.ru/window_size/2/index.html
    У вас есть 2 списка с размерами  size_x и size_y;
    При сочетании размеров из этих списков, появится число;
    Результат появится в id="result";
    Скопируйте результат в поле для ответа.

ps. При написании кода, учитывайте размер рамок браузера.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome(options=options) as browser:
    browser.get('http://parsinger.ru/window_size/2/index.html')
    for x in window_size_x:
        for y in window_size_y:
            browser.set_window_size(x, y)
            print(f'x={x}, y={y}, real size={browser.get_window_size()}')
            print(browser.find_element(By.ID, 'result').text)
            sleep(1)

