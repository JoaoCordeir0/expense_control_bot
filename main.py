from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from bot.config import BOT_TOKEN, ENV
from bot.texts import *
from bot.handlers import *
from bot.db import init_db
import re

def main():   
    init_db()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & filters.UpdateType.EDITED_MESSAGE, handle_edited_message))
    app.add_handler(CommandHandler('start', handle_start))
    app.add_handler(CommandHandler('ajuda', handle_help))
    app.add_handler(CommandHandler('suporte', handle_support))
    app.add_handler(CommandHandler('ativar', handle_active_user))
    app.add_handler(CommandHandler('resumo', handle_summary))
    app.add_handler(CommandHandler('calcular', handle_calculate_salary))
    app.add_handler(CommandHandler('grafico', handle_summary_chart))
    app.add_handler(
        MessageHandler(
            filters.TEXT & filters.Regex(re.compile(r'^gastei\s+\d+', re.IGNORECASE)),
            handle_register_expense
        )
    )
    app.add_handler(MessageHandler(filters.COMMAND, handle_help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_unknown_message))
    app.add_handler(CallbackQueryHandler(handle_callback))
    
    app.add_error_handler(lambda update, context: context.bot.send_message(
        chat_id=update.effective_chat.id if update and update.effective_chat else None,
        text=ERROR_MESSAGE
    ))

    print(f'Bot `{ENV}` iniciado.')

    app.run_polling()

if __name__ == '__main__':
    main()