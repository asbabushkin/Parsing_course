"""
7.4 Парсим данные участников группы

    Есть список lst=[] в котором хранятся username участников группы; https://t.me/Parsinger_Telethon_Test
    Цель собрать числа из поля "О Себе" или "About" пользователя из списка lst=[],
    затем суммировать все добытые числа;
    Полученное число вставить в поле для ответа.
"""
from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
from telegram_data import telegram_api, telegram_hash

r_api = telegram_api
r_hash = telegram_hash

lst = ['daxton_13246', 'Anthony_Alexander534', 'William_Price34', 'Roger_Parks4', 'Nancy_Montgomery54',
       'Melissa_Simmons4', 'Shane_Morris34', 'Gloria_Thompson4', 'Linda_Hernandez4',
       'Constance_Jones4', 'Joshua_Andrews34', 'Erica_Moore34', 'Timothy_Green3', 'Lisa_Hawkins',
       'Nancy_Johnson3', 'Mary_Davis1', 'Brian_Johnson2', 'Peter_Barnes', 'James_Washington3']

summa = 0

with TelegramClient('my', r_api, r_hash) as client:
    users = client.iter_participants('t.me/Parsinger_Telethon_Test')
    for user in users:
        if user.username in lst:
            user_full_about = client(GetFullUserRequest(user))
            if user_full_about.about:
                summa += int(user_full_about.about)
    print(summa)