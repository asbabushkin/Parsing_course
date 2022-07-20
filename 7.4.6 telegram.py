"""
7.4 Парсим данные участников группы https://t.me/Parsinger_Telethon_Test
    Скачайте полноразмерные аватарки всех участников группы;
    Встроенными методами windows узнайте общий размер всех аватарок;
    Полученное число в байтах вставьте в поля для ответа.


"""
from telethon import TelegramClient, events, sync, connection
from telegram_data import telegram_api, telegram_hash

r_api = telegram_api
r_hash = telegram_hash

with TelegramClient('my', r_api, r_hash) as client:
    participants = client.get_participants('t.me/Parsinger_Telethon_Test')
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f'D:\Python\Parsing_course\\telegrm_photos\{i}')