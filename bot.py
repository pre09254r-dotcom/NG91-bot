import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 NG91 Match Detection Bot\n\n"
        "Το bot είναι online!\n"
        "Σύντομα θα προσθέσουμε την αυτόματη ανίχνευση αγώνων."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot λειτουργεί κανονικά.")


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN δεν έχει οριστεί.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("🤖 Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
