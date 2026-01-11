import os
from dotenv import load_dotenv

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN not found in .env file")

# Main menu keyboard
main_menu_keyboard = ReplyKeyboardMarkup(
    [
        ["🐕 Banho e Tosa", "💉 Vacinas"],
        ["🕒 Horário", "📍 Endereço"],
        ["💬 Falar com atendente"],
    ],
    resize_keyboard=True,
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        "🐾 Bem-vindo ao *PetShop Amigo Fiel*!\n\n" "Escolha uma opção abaixo 👇",
        reply_markup=main_menu_keyboard,
        parse_mode="Markdown",
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages from users"""
    user_message = update.message.text.lower()

    if "banho" in user_message:
        await update.message.reply_text(
            "🐕 Banho e tosa a partir de R$ 50.\n"
            "Valores variam conforme o porte do pet."
        )

    elif "vacina" in user_message:
        await update.message.reply_text(
            "💉 Trabalhamos com vacinas V8, V10 e antirrábica.\n"
            "Aplicação com veterinário."
        )

    elif "horário" in user_message:
        await update.message.reply_text(
            "🕒 Horário de funcionamento:\n"
            "Segunda a Sexta: 9h às 18h\n"
            "Sábado: 9h às 14h"
        )

    elif "endereço" in user_message:
        await update.message.reply_text(
            "📍 Rua dos Pets, nº 123\n" "Centro – Sua Cidade"
        )

    elif "atendente" in user_message:
        await update.message.reply_text(
            "💬 Um atendente humano entrará em contato em breve.\n"
            "📞 WhatsApp: (11) 99999-9999"
        )
        # Example: forward message to admin or support group
        # await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=user_message)

    else:
        await update.message.reply_text(
            "❓ Não entendi sua mensagem.\n"
            "Por favor, escolha uma opção do menu abaixo 👇",
            reply_markup=main_menu_keyboard,
        )


def main():
    """Application entry point"""
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("🤖 PetShop bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
