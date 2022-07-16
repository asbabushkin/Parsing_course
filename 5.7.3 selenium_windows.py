"""
5.7 Окна и вкладки
    Откройте сайт при помощи Selenium; http://parsinger.ru/blank/modal/3/index.html
    На сайте есть 100 buttons;
    При нажатии на любую кнопку появляется confirm с пин-кодом;
    Текстовое поле под кнопками проверяет правильность пин-кода;
    Ваша задача, найти правильный пин-код и получить секретный код;
    Вставьте секретный код в поле для ответа.
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument(r'--user-data-dir=C:\Users\asbab\AppData\Local\Google\Chrome\User Data')
options_chrome.add_argument(r'--profile-directory=Default')

url1 = 'https://parsinger.ru/blank/modal/3/index.html'
RESULT = ''

def get_code(btn, brwsr):
    btn.click()
    sleep(0.5)
    window = brwsr.switch_to.alert
    sleep(0.5)
    code = window.text
    sleep(0.5)
    window.accept()
    sleep(0.5)
    return code


def check_code(brwsr):
    brwsr.find_element(By.ID, 'check').click()
    sleep(1)
    result = brwsr.find_element(By.ID, 'result').text
    if result == 'Неверный пин-код':
        return False
    else:
        print(result)
        return True, result


with webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options_chrome) as browser:
    browser.get(url1)
    sleep(1)
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    sleep(1)
    for b in buttons:
        browser.find_element(By.ID, 'input').send_keys(get_code(b, browser))
        sleep(1)
        if not check_code(browser):
            continue
        else:
            break

with webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe', chrome_options=options_chrome) as browser:
    browser.get(url='https://stepik.org/lesson/720527/step/3?auth=login&unit=721524')
    sleep(2)
    browser.find_element(By.CLASS_NAME, 'number-quiz__input number-input').send_keys('hello!')
    sleep(5)
