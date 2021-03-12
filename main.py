from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import re

def start(update,context): 
    user = update.message.from_user 
    send = f"{user.username} started you bot.\n First name {user.first_name}\n ID:{user.id}" 
    context.bot.send_message(chat_id = user.id,text = send) 
    update.message.reply_text('Hi')

TOKEN = "1503511812:AAGV8h4kSnDmvdz7eVpStAGcEuWrCh_uJC0"

BAD_WORDS = ["fuck","bitch","bugs","errors","ass"]

def bad_words_filter(input_string):
    for bad_word in BAD_WORDS:
        input_string = input_string.replace(bad_word, "***")
    return input_string

def num_to_words(number):
    a = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", \
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    b = ("", "","twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety")
    c = ("million", "thousand", "")
    if number == 0:
        return "null"
    elif number > 999999999:
        return "out of range"
    else:
        rezult = ""
        divider = 1000000
        for degree in c: 
            num_loc = int(number / divider)
            divider = divider / 1000
            if num_loc > 0:
                hundreds = int(num_loc / 100) % 10
                remainder = num_loc % 100
                if hundreds > 0:
                    rezult = rezult + " " + a[hundreds] + " hundred"
                    if hundreds > 1:
                        rezult += "s"
                    rezult = rezult + " and"
                if remainder < 20:
                    rezult = rezult + " " + a[remainder]
                else:
                    rezult = rezult + " " +  b[int(remainder / 10)]
                    if remainder % 10 != 0:
                        rezult = rezult + " " +  a[remainder % 10]
                rezult = rezult + " " + degree

        return rezult
    return "error"

def calc_expression(input_string):
    reg_multiply = re.findall(r"\d+[\*\/]\d+",input_string)
    while reg_multiply != []:
        if reg_multiply[0].find('*') > 0:
            n1 = re.findall(r"\d+\*",reg_multiply[0])[0][:-1]
            n2 = re.findall(r"\*\d+",reg_multiply[0])[0][1:]
            rezult = int(n1) * int(n2)
        else:
            n1 = re.findall(r"\d+\/",reg_multiply[0])[0][:-1]
            n2 = re.findall(r"\/\d+",reg_multiply[0])[0][1:]
            rezult = int(int(n1) / int(n2))

        input_string = input_string.replace(reg_multiply[0], str(rezult))
        reg_multiply = re.findall(r"\d+[\*\/]\d+",input_string)
    reg_substract = re.findall(r"\d+[\-\+]\d+",input_string)
    while reg_substract != []:
        if reg_substract[0].find('-') > 0:
            n1 = re.findall(r"\d+\-",reg_substract[0])[0][:-1]
            n2 = re.findall(r"\-\d+",reg_substract[0])[0][1:]
            rezult = int(n1) - int(n2)
        else:
            n1 = re.findall(r"\d+\+",reg_substract[0])[0][:-1]
            n2 = re.findall(r"\+\d+",reg_substract[0])[0][1:]
            rezult = int(n1) + int(n2)
        input_string = input_string.replace(reg_substract[0], str(rezult))
        reg_substract = re.findall(r"\d+[\-\+]\d+",input_string)
    return input_string

# print(calc_expression("1+5*6/2-3"))

def words_filter_handler(update,context): 
    update.message.reply_text(bad_words_filter(update.message.text))

def num_to_words_handler(update,context): 
    update.message.reply_text(num_to_words(int(update.message.text)))

def calc_expression_handler(update,context): 
    update.message.reply_text(calc_expression(update.message.text))

updater = Updater(TOKEN,use_context=True) 
dp = updater.dispatcher

dp.add_handler(CommandHandler("start",start))
dp.add_handler(MessageHandler(Filters.regex('^filter '),words_filter_handler))
dp.add_handler(MessageHandler(Filters.regex('^[0-9]*'),num_to_words_handler))
dp.add_handler(MessageHandler(Filters.regex(r'^(\d+[\+\-\*\/]\d+){1}([\+\-\*\/]+\d+)*$'), calc_expression_handler))

updater.start_polling() 
updater.idle()