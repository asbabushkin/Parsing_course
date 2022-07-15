"""
5.6 Скроллинг страниц
    Откройте сайт сайт с помощью Selenium; http://parsinger.ru/scroll/3/
    Ваша задача, получить числовое значение  id="число" с каждого тега <input> который при нажатии вернул число;
    Суммируйте все значения и отправьте результат в поле ниже.
"""
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

summa = 0

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/3/')
    input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]
    count = 1
    for inp in input_tags:

        inp.send_keys(Keys.DOWN)
        try:
            inp.click()
            WebDriverWait(webdriver, 10).until(EC.element_to_be_selected(inp))
        except TimeoutException:
            inp.click()
            WebDriverWait(webdriver, 10).until(EC.element_to_be_selected(inp))
        finally:
            inp_id = inp.get_attribute('id')
            secret = browser.find_element(By.ID, f'result{inp_id}').text
            if secret:
                summa += int(inp_id)
            count += 1

    print(summa)

