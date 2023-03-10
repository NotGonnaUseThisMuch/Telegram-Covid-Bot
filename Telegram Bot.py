import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

updater = Updater(token= '6077839509:AAE0LsHm1dxsjZiKcTY8KHFSQkoze-aM41s', use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text = "Hello, World")
    
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

updater.start_polling()

def summary(update, context):
    response = requests.get("https://api.covid19api.com/summary")
    if (response.status_code==200):
        data = response.json()
        date = data['Date'][:10]
        ans = f"Covid 19 summary (as of {date}): \n"
        
        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed','NewDeaths', 'NewRecovered']:
                ans += 'Total' + attribute[5::].lower() + ":" + str(value) + "\n"
        
        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong")

summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(summary_handler)

#Telegram Bot HW - Basic Info Bot   
    
    
    
    