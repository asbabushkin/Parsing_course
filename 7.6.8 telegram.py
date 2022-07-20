"""
7.4 Парсим данные участников группы
    Скачайте полноразмерные аватарки всех участников группы включая все сохранённые аварки;
    Встроенными методами windows узнайте общий размер всех аватарок;
    Полученное число в байтах вставьте в поля для ответа.
"""

from telethon import TelegramClient, events, sync, connection
from telegram_data import telegram_api, telegram_hash

r_api = telegram_api
r_hash = telegram_hash

with TelegramClient('my', r_api, r_hash) as client:
    all_user_group = client.get_participants('t.me/Parsinger_Telethon_Test')
    for user in all_user_group:
        for photo in client.iter_profile_photos(user):
            client.download_media(photo, file=f'D:\Python\Parsing_course\\telegrm_photos\\task2\img')