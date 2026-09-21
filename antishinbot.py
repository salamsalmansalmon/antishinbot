import logging
from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
bot_username: Final = '@antishin_bot'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Shin hunter readys"
    )

#antishin command
async def antisnipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trigger = 'to your harem by sending'
    message = update.message.text
    if 'to your harem by sending' in message.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='/tmute @Shinzex 5m')


if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)

    antisnipe_Handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND),
        antisnipe
    )

    application.add_handler(start_handler)
    application.add_handler(antisnipe_Handler)

    application.run_polling()
