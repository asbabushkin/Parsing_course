"""
5.7 Окна и вкладки
    Откройте сайт при помощи Selenium; http://parsinger.ru/blank/modal/4/index.html
    На сайте есть список пин-кодов и только один правильный;
    Для проверки пин-кода используйте кнопку "Проверить"
    Ваша задача, найти правильный пин-код и получить секретный код;
    Вставьте секретный код в поле для ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/4/index.html')
    pins = browser.find_elements(By.CLASS_NAME, 'pin')
    check_btn = browser.find_element(By.ID, 'check')

    for p in pins:
        code = p.text
        check_btn.click()
        modal_window = browser.switch_to.alert
        modal_window.send_keys(code)
        modal_window.accept()
        res = browser.find_element(By.ID, 'result').text
        if res == 'Неверный пин-код':
            continue
        else:
            print(res)
            break
