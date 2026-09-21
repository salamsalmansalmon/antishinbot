import logging
from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import html
from typing import Optional, List
from datetime import datetime, timedelta
from telegram import Message, Chat, Bot, User
from telegram.error import BadRequest
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import mention_html

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.helper_funcs.chat_status import bot_admin, user_admin, is_user_admin, can_restrict
from tg_bot.modules.helper_funcs.extraction import extract_user, extract_user_and_text
from tg_bot.modules.helper_funcs.string_handling import extract_time
from tg_bot.modules.log_channel import loggable

TOKEN = os.getenv("BOT_TOKEN")


application = ApplicationBuilder().token(TOKEN).build()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Shin hunter ready sires"
    )
#mutetime settings
mutetime = datetime.now() + timedelta(seconds=30)
chat = 'jawa'
user_id = 'timur'

#antishin command
async def antisnipe(bot: Bot, update: Update, context: ContextTypes.DEFAULT_TYPE):
    trigger = 'to your harem by sending'
    message = update.message.text
    if 'to your harem by sending' in message.lower():
        await bot.restrict_chat_member(chat.id, user_id, until_date=mutetime, can_send_messages=False)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='@Shinzex has been muted')

#get_user_id_command
async def get_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.reply_to_message:
        target_user = update.message.reply_to_message.from_user
        name = target_user.full_name
        user_id = target_user.id
        username = f"@{target_user.username}" if target_user.username else "No public username"
        response = (
            f"👤 User Info (Replied)\n"
            f"🔹 Name: {name}\n"
            f"🔹 Username: {username}\n"
            f"🆔 User ID: {user_id}"
        )
        await update.message.reply_text(response, parse_mode="Markdown")
    else:
        # If not a reply, return the ID of the person who typed the command
        sender = update.message.from_user
        response = (
            f"ℹ️ Reply to someone's message with /id to get their ID.\n"
            f"Your own ID is: {sender.id}"
        )
        await update.message.reply_text(response, parse_mode="Markdown")



if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)

    antisnipe_Handler = MessageHandler(
        filters.TEXT,
        antisnipe
    )
    get_user_id_handler = CommandHandler("getid", get_user_id)
    application.add_handler(start_handler)
    application.add_handler(antisnipe_Handler)
    application.add_handler(get_user_id_handler)
    application.run_polling()
