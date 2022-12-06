from telegram.ext import ApplicationBuilder, CommandHandler
from bot_coomands import *

token = import_from_file('token.txt')

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("Server start")

app.run_polling()