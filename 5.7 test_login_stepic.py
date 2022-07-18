from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from auth_data import stepik_login, stepik_pswd

ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={ua.random}')

with webdriver.Chrome(options=options) as step_driver:
    step_driver.get(url='https://stepik.org/learn?auth=login')
    sleep(1)
    login = step_driver.find_element(By.ID, 'id_login_email')
    sleep(1)
    password = step_driver.find_element(By.ID, 'id_login_password')
    sleep(1)

    login.send_keys(stepik_login)
    sleep(1)

    password.send_keys(stepik_pswd)
    sleep(1)
    password.send_keys(Keys.ENTER)
    #step_driver.find_element(By.CLASS_NAME, "sign-form__btn button_with-loader ").click()
    sleep(5)
    step_driver.get('https://stepik.org/lesson/720527/step/6?unit=721524')
    sleep(10)
