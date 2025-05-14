from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.config import BOT_TOKEN, ENV
from bot.handlers import *
from bot.db import init_db
import re

def main():   
    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('ajuda', help))
    app.add_handler(CommandHandler('suporte', support))
    app.add_handler(CommandHandler('ativar', active_user))
    app.add_handler(CommandHandler('resumo', summary))
    app.add_handler(CommandHandler('grafico', summary_chart))
    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex(re.compile(r'^gastei\s+\d+', re.IGNORECASE)),
            register_expense
        )
    )
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    print(f'Bot `{ENV}` iniciado.')
    app.run_polling()

if __name__ == '__main__':
    main()