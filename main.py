from telegram import Update, Message, User, CallbackQuery,InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters
import os
from codewars import User, Users
from pprint import pprint
import csv
from photo import JPG

TOKEN = os.getenv('CODEWARS')
app = ApplicationBuilder().token(TOKEN).build()




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyord = [[InlineKeyboardButton("Assalomu alaykum", url="https://t.me/Dilmurod_Kitob_haqida_blog")]
    ]

    reply_markup = InlineKeyboardMarkup(keyord)
    await update.message.reply_text("Assalomu alaykum!\nBotimizga hush kelibsiz!", reply_markup=reply_markup)

    keyboard = [[KeyboardButton("2024 PYTHON #1"), KeyboardButton("Codewars RESULTS"),KeyboardButton("python_5")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Qaysi guruhning natijalari kerak", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    async def doIt(text):
        await update.message.reply_text(f"Biz codewarsdan {text} guruhning natijalarni olmoqdamiz\niltimos kuting")

        group = text.replace(" ",'')
        users = [
        
        ]
        def dict_to_csv(data, path):
            with open(path, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
           
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
        dailycsv = f'{group}_daily.csv'
        weeklycsv = f'{group}_weekly.csv'

        dict_to_csv(daily,dailycsv)
        dict_to_csv(weekly,weeklycsv)


        JPG(f"{dailycsv}",f"{group}d.jpg")
        JPG(f"{weeklycsv}",f"{group}w.jpg")


        await update.message.reply_photo(f"{group}d.jpg")
        await update.message.reply_text(f"#daily")

        await update.message.reply_photo(f"{group}w.jpg")
        await update.message.reply_text(f"#weekly")

    if text == "Codewars RESULTS":
        await doIt(text)
    elif text == "2024 PYTHON #1":
        await doIt(text)
    elif text == "python_5":
        await doIt("python_5")
    else:
        await update.message.reply_text("Bizda bunaqa guruhning ro'yxati yo'q\niltimos pastdagi guruhlardan birini tanlang!")

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()