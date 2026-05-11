import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your Bot Token
TOKEN = '8138447285:AAEi8XRSkuqPjy8Gks7oQwmZjoF47Wvo-SM'

# Battery status function
async def battery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = subprocess.getoutput("termux-battery-status")
    await update.message.reply_text(f"Current Battery Status:\n{status}")

# Photo capturing function
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Capturing photo, please wait...")
    os.system("termux-camera-photo -c 0 photo.jpg")
    if os.path.exists("photo.jpg"):
        await update.message.reply_photo(photo=open('photo.jpg', 'rb'))
    else:
        await update.message.reply_text("Error: Could not capture photo. Ensure Termux:API is installed.")

# Vibrate function
async def vibrate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    os.system("termux-vibrate -d 1000")
    await update.message.reply_text("Phone vibrated successfully!")

# Start command message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu = (
        "Bot is Online!\n\n"
        "Commands:\n"
        "/battery - View battery info\n"
        "/photo - Take a back camera picture\n"
        "/vibrate - Vibrate the phone\n"
    )
    await update.message.reply_text(menu)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("battery", battery))
    app.add_handler(CommandHandler("photo", photo))
    app.add_handler(CommandHandler("vibrate", vibrate))
    
    print("Bot is running... Send commands to your Telegram Bot.")
    app.run_polling()

