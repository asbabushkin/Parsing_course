import requests

url = 'http://httpbin.org'
response = requests.get(url)
print(response.status_code)