import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', default='')
MY_CHAT_ID = os.getenv('MY_CHAT_ID', default='')
