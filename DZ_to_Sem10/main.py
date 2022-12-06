from telegram.ext import ApplicationBuilder, CommandHandler
from bot_coomands import *

app = ApplicationBuilder().token("5834653879:AAHe6BnTUvJ2ZpxLhNjbFdj0VmV8u1pkUb4").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
print("Server start")

app.run_polling()