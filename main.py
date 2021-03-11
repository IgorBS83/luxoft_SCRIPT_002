from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,ConversationHandler 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def start(update,context): 
    user = update.message.from_user 
    send = f"{user.username} started you bot.\n First name {user.first_name}\n ID:{user.id}" 
    context.bot.send_message(chat_id = user.id,text = send) 
    update.message.reply_text('Hi')

TOKEN = "1503511812:AAGV8h4kSnDmvdz7eVpStAGcEuWrCh_uJC0"

BAD_WORDS = ["fuck","bitch","nigga","bugs","errors"]

def bad_words_filter(input_string):
    local_string = input_string
    for bad_word in BAD_WORDS:
        local_string.replace(bad_word, "***")
        pos = local_string.find(bad_word)
    return local_string

aaa="aad fuck asdf"
print(bad_words_filter(aaa))
# def words_filter_handler(update,context): 
#     update.message.reply_text(bad_words_filter(update.message.text))

# updater = Updater(TOKEN,use_context=True) 
# dp = updater.dispatcher

# dp.add_handler(CommandHandler("start",start))
# dp.add_handler(MessageHandler(Filters.regex('^filter '),words_filter_handler))

# updater.start_polling() 
# updater.idle()