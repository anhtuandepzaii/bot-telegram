from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Xin chào! Tôi là bot của bạn.')

if __name__ == '__main__':
    app = ApplicationBuilder().token("7592545143:AAHLXtdfIs78_lv2I6ij9i2JmFr7yRCJ8fk").build()

    app.add_handler(CommandHandler("start", start))

    print("Bot đang chạy . . .")
    app.run_polling()
    print("Bot đã dừng")