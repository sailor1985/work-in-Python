from telegram import Update
from telegram.ext import CallbackContext


def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()


def import_from_file(filename: str):  # Чтение из текстового файла. Вход:строка. Выход:строка
    with open(filename, "r") as data:
        a = data.read()
    return a
