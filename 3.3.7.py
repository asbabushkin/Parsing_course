"""
Задача:

    Перейдите на сайт http://parsinger.ru/video_downloads/
    Скачайте видео с сайта  при помощи requests
    Определите его размер в ручную
    Напишите размер файла в поле для ответа. Написать нужно только цифру в мб.

"""

import requests

URL = 'http://parsinger.ru/video_downloads/videoplayback.mp4'
response = requests.get(url=URL, stream=True)
with open('file.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=102400):
        video.write(piece)
