from telethon import TelegramClient, events, sync, connection
from telegram_data import telegram_api, telegram_hash


api_id = telegram_api
api_hash = telegram_hash

client = TelegramClient('session_name', api_id, api_hash)
client.start()
print(client.get_me())