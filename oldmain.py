import logging
from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import html
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram.error import BadRequest
from telegram.ext import CommandHandler, Filters
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.helper_funcs.chat_status import bot_admin, user_admin, is_user_admin, can_restrict
from tg_bot.modules.helper_funcs.extraction import extract_user, extract_user_and_text
from tg_bot.modules.helper_funcs.string_handling import extract_time
from tg_bot.modules.log_channel import loggable
TOKEN = os.getenv("BOT_TOKEN")

if TOKEN is None:
    raise ValueError("BOT_TOKEN belum ditemukan di environment variables")

application = ApplicationBuilder().token(TOKEN).build()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Shin hunter ready sire"
    )

#antishin command
async def antisnipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trigger = 'to your harem by sending'
    message = update.message.text
    if 'to your harem by sending' in message.lower():
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='/tmute@MissRose_bot @Shinzex 5m')


if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)

    antisnipe_Handler = MessageHandler(
        filters.TEXT,
        antisnipe
    )

    application.add_handler(start_handler)
    application.add_handler(antisnipe_Handler)

    application.run_polling()
