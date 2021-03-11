from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import re

def start(update,context): 
    user = update.message.from_user 
    send = f"{user.username} started you bot.\n First name {user.first_name}\n ID:{user.id}" 
    context.bot.send_message(chat_id = user.id,text = send) 
    update.message.reply_text('Hi')

TOKEN = "1503511812:AAGV8h4kSnDmvdz7eVpStAGcEuWrCh_uJC0"

BAD_WORDS = ["fuck","bitch","nigga","bugs","errors","ass"]

def bad_words_filter(input_string):
    for bad_word in BAD_WORDS:
        input_string = input_string.replace(bad_word, "***")
    return input_string

def num_to_words(number):
    str_number = str(number)
    rezult = ""
    digit = str_number[-1]
    if str_number == '0':
        rezult = "null"
    elif digit == '1':
        rezult = "one"
    elif digit == '2':
        rezult = "two"
    elif digit == '3':
        rezult = "three"
    elif digit == '4':
        rezult = "four"
    elif digit == '5':
        rezult = "five"
    elif digit == '6':
        rezult = "six"
    elif digit == '7':
        rezult = "seven"
    elif digit == '8':
        rezult = "eight"
    elif digit == '9':
        rezult = "nine"
    if digit != str_number:
        digit = str_number[-2:-1]
        if digit == '1':
            if str_number[-2:] == "10":
                rezult = "ten"
            elif str_number[-2:] == "11":
                rezult = "eleven"
            elif str_number[-2:] == "12":
                rezult = "twelve"
            else: 
                rezult = rezult + "teen"
        elif digit == '2':
            rezult = "twenty" + rezult
        elif digit == '3':
            rezult = "thirty " + rezult
        elif digit == '4':
            rezult = "fourty " + rezult
        elif digit == '5':
            rezult = "fifty " + rezult
        elif digit == '6':
            rezult = "sixty " + rezult
        elif digit == '7':
            rezult = "seventy " + rezult
        elif digit == '8':
            rezult = "eighty " + rezult
        elif digit == '9':
            rezult = "ninety "   + rezult 
    return rezult

def calc_expression(input_string):
    r1 = re.findall(r"\d+\*\d+",input_string)
    n1 = re.findall(r"\d+\*",input_string)
    print(n1)
    n1 = n1[:-1]
    print(n1)
    print(r1)
    # return r1

calc_expression("25+658*45+1")
#  print(calc_expression("25+658*45+1"))
# print(num_to_words(12))
# print(num_to_words(11))
# print(num_to_words(10))
# print(num_to_words(9))
# print(num_to_words(14))

# def words_filter_handler(update,context): 
#     update.message.reply_text(bad_words_filter(update.message.text))

# def num_to_words_handler(update,context): 
#     update.message.reply_text(num_to_words(int(update.message.text)))

# def calc_expression_handler(update,context): 
#     update.message.reply_text(calc_expression(update.message.text))

# updater = Updater(TOKEN,use_context=True) 
# dp = updater.dispatcher

# dp.add_handler(CommandHandler("start",start))
# dp.add_handler(MessageHandler(Filters.regex('^filter '),words_filter_handler))
# dp.add_handler(MessageHandler(Filters.regex('^[0-9]*'),num_to_words_handler))
# dp.add_handler(MessageHandler(Filters.regex(r'^(\d+[\+\-\*\/]\d+){1}([\+\-\*\/]+\d+)*$'), calc_expression_handler))

# updater.start_polling() 
# updater.idle()