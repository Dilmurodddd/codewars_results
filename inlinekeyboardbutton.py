from telegram import Update, Message, User, CallbackQuery,InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters
import os
from codewars import User, Users
from pprint import pprint
import csv

TOKEN = os.getenv('CODEWARS')
app = ApplicationBuilder().token(TOKEN).build()




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyord = [[InlineKeyboardButton("Codewars RESULTS", callback_data="Codewars RESULTS")],
              [InlineKeyboardButton("2024 PYTHON #1", callback_data="2024 PYTHON #1")]
    ]

    reply_markup = InlineKeyboardMarkup(keyord)
    await update.message.reply_text("Assalomu alaykum!\nBotimizga hush kelibsiz!\nQaysi guruhning natijalari kerak?", reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    query = update.callback_query
    if query.data == "Codewars RESULTS":
        await query.edit_message_text(text=f"Siz bosdingiz: {query.data}")

        await query.message.reply_text(f"Biz codewarsdan {query.data} guruhning natijalarni olmoqdamiz\niltimos kuting")
 
        group ='python_0'
        users = [
        
        ]
        
        with open(f'group/{group}.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append({
                    'username': row['username'],
                    'fullname': row['fullname']
                })
        
        users = Users(users)
        
        daily=users.get_total_daily()
        weekly = users.get_total_weekly()
        d = ""
        w = ""
        for i in daily:
            d += f"{i['name']} - {i['total_completed']}\n"
        for i in weekly:
            w += f"{i['name']} - {i['total_completed']}\n"
        await query.message.reply_text(f"Daily \n{d}\nWeekly \n{w}")
    elif query.data == "2024 PYTHON #1":
        await query.edit_message_text(text=f"Siz bosdingiz: {query.data}")

                
        await query.message.reply_text(f"Biz codewarsdan {query.data} guruhning natijalarni olmoqdamiz\niltimos kuting")
        group ='python_2'
        users = [
                
        ]
                
        with open(f'group/{group}.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append({
                    'username': row['username'],
                    'fullname': row['fullname']
                })
                
        users = Users(users)
                
        daily=users.get_total_daily()
        weekly = users.get_total_weekly()
        d = ""
        w = ""
        for i in daily:
            d += f"{i['name']} - {i['total_completed']}\n"
        for i in weekly:
            w += f"{i['name']} - {i['total_completed']}\n"
        await query.message.reply_text(f"Daily \n{d}\nWeekly \n{w}")

app.add_handler(CallbackQueryHandler(button_callback))
app.add_handler(CommandHandler("start", start))
app.run_polling()
