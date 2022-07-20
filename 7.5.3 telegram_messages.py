"""
7.5 Парсим сообщения группы

    Спарсить числовые значения из сообщений в группе; https://t.me/Parsinger_Telethon_Test
    Суммировать полученные числа и вставить результат в поле для ответа.
"""

from telethon import TelegramClient
from telegram_data import telegram_api, telegram_hash

summa = 0

with TelegramClient('my', telegram_api, telegram_hash) as client:
    all_message = client.get_messages('https://t.me/Parsinger_Telethon_Test', limit=1000)
    for message in all_message:
        if message.message:
            summa += int(message.message)
    print(summa)