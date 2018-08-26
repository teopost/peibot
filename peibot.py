#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import datetime
import botogram
import os

bot_token = os.environ.get("PEI_BOT_TOKEN")
staff_chat_id = os.environ.get("PEI_STAFF_CHAT_ID")


if not bot_token or not staff_chat_id:
    print("Config unavailable.")

bot = botogram.create(bot_token)


@bot.command("info")
def hello_command(chat, message, args):
    """Welcome to Telegram File System
    """
    btns = botogram.Buttons()
    # btns[0].callback("Prenota un appuntamento", "prenota")
    # chat.send("Benvenuto al Pei - chat.id: " + str(chat.id), attach=btns)
    chat.send("chat_id: " + str(chat.id))


@bot.command("start")
def hello_command(chat, message, args):
    """Welcome to Pei Support Bot
    """
    # btns = botogram.Buttons()
    # btns[0].callback("Prenota un appuntamento", "prenota")
    # chat.send("Benvenuto al Pei - chat.id: " + str(chat.id), attach=btns)
    # chat.send("Benvenuto al Pei - chat.id: " + str(chat.id))


@bot.process_message
def process_message(chat, message):
    # group chat id: -1001203228278
    # personal chat id: 2438719
    if chat.type == "private":
        message.forward_to(staff_chat_id)
    else:
        reply_id = message.reply_to_message.forward_from.id

        if message.photo is not None:
            print (">>>" + str(message.photo.file_id))
            bot.chat(reply_id).send_photo(
                file_id=message.photo.file_id,
                caption=message.caption)
        else:
            bot.chat(reply_id).send(message.text)

    if message.sender != chat.creator:
        message.reply("You're not the creator of the chat")

    # chat.send("ripeto:"+ chat.type + "," + chat.sender.username + "
    # chat.id: " + str(chat.id))


if __name__ == "__main__":
    bot.run()
