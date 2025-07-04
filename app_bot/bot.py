import os
import django
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Django if not already configured
try:
    django.setup()
except Exception:
    pass  # Django might already be configured

from app_account.models import User
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from asgiref.sync import sync_to_async

BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = os.getenv('BASE_URL')


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

@sync_to_async
def save_user(user):
    theUser , created =  User.objects.get_or_create(
        telegram_username=user.username,
        telegram_full_name=user.full_name,
        telegram_id=user.id,
        is_active=True,
        is_admin=False,

    )
    if created:
        # we will create a wallet for the user
        pass
    theUser.save()

    return theUser







async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = await save_user(update.effective_user)
    await update.message.reply_text(f"Hello {user.telegram_full_name}! Welcome to the bot. Please use the /help command to get started.")


def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not found in environment variables")
        return
    
    try:
        # Create the Application and pass it your bot's token.
        application = Application.builder().token(BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", start))

        logger.info("Bot started successfully")
        # Run the bot until the user presses Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise


if __name__ == "__main__":
    main()