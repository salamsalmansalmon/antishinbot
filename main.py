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
from telegram import ChatPermissions


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



#antishin command
trigger_bot_ids = [
    1964681186,  # Collect_your_husbando_bot
    1733263647   # Bot kedua
]
async def antisnipe(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.effective_message

    if not message:
        return
    if not message.from_user:
        return
    if message.from_user.id not in trigger_bot_ids:
        return
    if not message.photo:
        return

    # Ambil text atau caption
    text = message.text or message.caption or ""

    print("=" * 50)
    print("MESSAGE DETECTED")
    print("Text/Caption:", repr(text))
    print("From:", message.from_user)
    print("Sender Chat:", message.sender_chat)
    print("Has photo:", bool(message.photo))
    print("=" * 50)

    trigger = "to your harem by sending"

    if trigger in text.lower():

        chat_id = update.effective_chat.id
        user_shin = 5984259599
        mutetime = datetime.now() + timedelta(seconds=60)
        permissions = ChatPermissions(
        can_send_messages=False
        )
        try:


            await context.bot.restrict_chat_member(
                chat_id=chat_id,
                user_id=user_shin,
                until_date=mutetime,
                permissions=permissions
)
            await context.bot.send_message(
                chat_id=chat_id,
                text="@Shinzex has been muted for 1 minute"
            )

        except BadRequest as e:

            print("Mute failed:", e)

            await context.bot.send_message(
                chat_id=chat_id,
                text=f"Failed to mute user: {e}"
            )
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
        (filters.PHOTO) & ~filters.COMMAND,
        antisnipe
    )
    get_user_id_handler = CommandHandler("getid", get_user_id)
    application.add_handler(start_handler)
    application.add_handler(antisnipe_Handler)
    application.add_handler(get_user_id_handler)
    application.run_polling()
