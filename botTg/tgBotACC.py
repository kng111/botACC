from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3
import datetime
import time
TOKEN = '6067485005:AAGbH2bP3KwTglHl9aH3achaEWrhvYET3Wk'

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id

    # Подключаемся к базе данных внутри функции
    with sqlite3.connect('sql.db') as conn:
        cursor = conn.cursor()

        user = update.effective_user
        user_id = user.id
        first_name = user.first_name
        last_name = user.last_name
        Fio = str(last_name) + str(first_name)
        username = user.username

        current_date = datetime.datetime.now().strftime('%m/%d')
        current_time = datetime.datetime.now().strftime('%H:%M:%S')

        # Проверяем, есть ли уже запись для этого пользователя сегодня
        cursor.execute('SELECT * FROM table1 WHERE login=? AND data LIKE ?', (username, f'%{current_date}%'))
        existing_user_today = cursor.fetchone()

        if existing_user_today:
            update.message.reply_text('\U0001F47E: Вы уже отмечены сегодня.')
            return

        cursor.execute('INSERT INTO table1 (login, data, name) VALUES (?, ?, ?)', (username, f'{current_date} {current_time}', Fio))
        update.message.reply_text(f'\U0001F47E: {Fio}, Вы отмечены на паре, в {current_time}')
        # Предположим, что date_str - это строка с датой в формате 'ГГГГ-ММ-ДД'
        cursor.execute('SELECT COUNT(*) FROM table1 WHERE data LIKE ?', (current_date + '%',))
        count = cursor.fetchone()[0]
        update.message.reply_text(f'\U0001F47E: Сейчас присутствуют - {count}.')





# Инициализация бота
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher

# Добавляем обработчик команды /start
dp.add_handler(CommandHandler('start', start))

# Запускаем бота
updater.start_polling()
updater.idle()
