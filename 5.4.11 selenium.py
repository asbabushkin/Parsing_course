"""
5.4 Поиск элементов Selenium

    Откройте сайт; http://parsinger.ru/selenium/4/4.html
    Установите все чек боксы в положение checked при помощи selenium и метода click();
    Когда все чек боксы станут активны, нажмите на кнопку;
    Скопируйте число которое появится на странице;
    Результат появится в <p id="result">Result</p>;
    Вставьте число в поле для ответа.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless')

# with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/4/4.html')
    cbx_list = browser.find_elements(By.CLASS_NAME, 'check')

    for cb in cbx_list:
        cb.click()

    browser.find_element(By.CLASS_NAME, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
    print(result)

