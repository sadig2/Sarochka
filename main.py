from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
import operator
from dotenv import load_dotenv
import os
load_dotenv()





load_dotenv(verbose=True)

update = Updater(token=os.getenv("TOKEN"))
dispatcher = update.dispatcher

def start(bot, update):
    bot.send_message(chat_id =update.message.chat_id, text= "Приветик я маленькая и умная Сарочка, я могу решать математические примерчики) задай мне вопрос")


start_handler=CommandHandler("start",start)
dispatcher.add_handler(start_handler)



def echo(bot, update): 

    input = update.message.text
    print(type(input))
    result = ""

    numbers = []
    op = ""

    print("here")

    words = input.split()

    for w in words:
        if (re.match('^\d*$',w)):
           numbers.append(w)

        if (re.match('\+',w)):
           op = w

        
        if (re.match('\-',w)):
           op = w

    print("here")

    answer = ""

    if (op == "+"):

        answer = str(int(numbers[0])+int(numbers[1]))
    elif (op == "-"):
        answer= str(int(numbers[0])-int(numbers[1]))

    
    result = "няяя решила))  {} {} {}  равняется {}".format(numbers[0],op,numbers[1],answer)
    print(input)

    bot.send_message(chat_id= update.message.chat_id, text = result)

echo_handler = MessageHandler(Filters.text,echo)

dispatcher.add_handler(echo_handler)

update.start_polling()

