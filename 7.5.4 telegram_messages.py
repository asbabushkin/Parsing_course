"""
7.5 Парсим сообщения группы

    В группе есть закреплённое сообщение; https://t.me/Parsinger_Telethon_Test
    Цель: получить user_id пользователя чьё сообщение закреплено;
    Вставить полученный user_id в поле для ответа.
"""
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPinned

from telegram_data import telegram_api, telegram_hash

with TelegramClient('my', telegram_api, telegram_hash) as client:
    all_messages = client.get_messages('https://t.me/Parsinger_Telethon_Test', filter=InputMessagesFilterPinned, limit=100)
    for message in all_messages:
        print(message.from_id.user_id)


