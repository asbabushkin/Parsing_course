"""

5.6 Скроллинг страниц
    Откройте сайт с помощью Selenium; https://parsinger.ru/scroll/2/index.html
    На сайте есть 100 чекбоксов, 25 из них вернут число;
    Ваша задача суммировать все появившиеся числа;
    Отправить получившийся результат в поля ответа.
"""


from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


summa = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')

    input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
    for inp in input_tags:
        inp.send_keys(Keys.DOWN)
        inp.click()

        inp_id = inp.get_attribute('id')
        secret = browser.find_element(By.ID, f'result{inp_id}').text
        if secret:
            summa += int(secret)

print(summa)
