#fake_useragent
import requests
from fake_useragent import UserAgent


url = 'http://httpbin.org/user-agent'
ua = UserAgent()

for x in range(10):
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)