from telegram.ext import *
from telegram import *
from telegram.ext.filters import Filters
import logging
import os
import re

def start(bot, update):
    update.message.from_user.send_message("Hewwo there Senpai owo")

def owo(bot,update):
    msgpreowo=update.message.reply_to_message.text
    msgmidowo=re.sub("[RL]","W",msgpreowo)
    msgmidowo=re.sub("[rl]","w",msgmidowo)
    msgmidowo=re.sub("n([aeiou])",r"ny\1",msgmidowo)
    msgmidowo=re.sub("N([AEIOU])",r"NY\1",msgmidowo)
    msgmidowo=re.sub("N([aeiou])",r"Ny\1",msgmidowo)
    msgmidowo=re.sub("([ao])^[a-zA-Z]",r"\1h",msgmidowo)
    msgmidowo=re.sub("([AO])^[a-zA-Z]",r"\1H",msgmidowo)
    msgpostowo=msgmidowo+" owo"
    bot.send_message(chat_id=update.message.chat_id,text=msgpostowo)


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    with open("TOKEN") as token_file:
        bot_token = token_file.read()
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)
  
    owo_handler=CommandHandler("owo", owo)
    dispatcher.add_handler(owo_handler)
    
 
  
   
    
   
    updater.start_polling()
    updater.idle()
