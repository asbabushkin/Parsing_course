import requests

URL = 'https://parsinger.ru/img_download/img/ready/160.png'

for i in range(10):
    response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png')
    # with open(f'{i}.png', 'wb') as file:
    with open(f'/media/sf_Python/Parsing_course/images/{i}.png', 'wb') as file:
        file.write(response.content)
