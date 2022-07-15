"""
5.4 Поиск элементов Selenium

    Откройте сайт при помощи selenium; http://parsinger.ru/selenium/6/6.html
    Решите уравнение на странице;
    Найдите и выберите в  выпадающем списке элемент с числом, которое у вас получилось
    после решения уравнения;
    Нажмите на кнопку;
    Скопируйте число и вставьте в поле ответа.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

num_raw = []


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    numbers = browser.find_elements(By.CLASS_NAME, 'num')
    for num in numbers:
        num_raw.append(num.text)
    result = int(num_raw[0][2:]) * int(num_raw[1][0]) * int(num_raw[2][0]) + int(num_raw[3])
    print(result)
    for option in browser.find_elements(By.TAG_NAME, 'option'):
        if option.text == str(result):
            browser.find_element(By.ID, 'selectId').send_keys(option.text)
            browser.find_element(By.ID, 'sendbutton').click()
            print(browser.find_element(By.ID, 'result').text)

            break

    sleep(10)







