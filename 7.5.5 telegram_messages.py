"""
7.5 Парсим сообщения группы
    В группе пользователь с user_id=5523594628 оставил несколько цифровых сообщений; https://t.me/Parsinger_Telethon_Test
    Цель: Определить участника с указанным user_id и получить его сообщения и суммировать их;
    Полученное число вставьте в поле для ответа.
"""
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPinned

from telegram_data import telegram_api, telegram_hash
summa = 0

with TelegramClient('my', telegram_api, telegram_hash) as client:
    all_messages = client.get_messages('https://t.me/Parsinger_Telethon_Test', limit=1000)
    for message in all_messages:
        print(message.text)

