from telethon import TelegramClient
from telegram_data import telegram_api, telegram_hash

r_api = telegram_api
r_hash = telegram_hash

client = TelegramClient('session_name2', r_api, r_hash)
client.start()
print(client.get_me())
participants = client.get_participants('t.me/Parsinger_Telethon_Test')
print(participants)
part_info = []
for p in participants:
    print(p.first_name, p.last_name)
    part_info.extend((p.id, p.first_name, p.last_name, p.phone))
print(part_info)
