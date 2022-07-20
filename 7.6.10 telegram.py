"""
7.4 Парсим данные участников группы

    Есть список lst=[] в котором хранятся ID участников группы; https://t.me/Parsinger_Telethon_Test
    Цель собрать числа из поля "О Себе" или "About" пользователя если его ID имеется в списке,
    затем суммировать все добытые числа;
    Полученное число вставить в поле для ответа.
"""
from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
from telegram_data import telegram_api, telegram_hash

r_api = telegram_api
r_hash = telegram_hash

lst = [5125814085, 5423813689, 5395359919, 5330282124, 5451738743, 5319101536,
       5599808192, 5552200609, 5560704798, 5421516684, 5596049016, 5313438049,
       5530400713, 5595171770, 5373895551, 5582701295, 5401839698, 5443556002,
       5445202221, 5394891665, 5486227453, 5342098799, 5486370067, 5576022537,
       5539803054, 5523594628, 5449816597, 5235694206]

summa = 0

with TelegramClient('my', r_api, r_hash) as client:
    users = client.iter_participants('t.me/Parsinger_Telethon_Test')
    for user in users:
        if user.id in lst:
            user_full_about = client(GetFullUserRequest(user))
            if user_full_about.about:
                summa += int(user_full_about.about)
    print(summa)
