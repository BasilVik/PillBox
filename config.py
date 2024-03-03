import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN', default='')
MY_CHAT_ID = os.getenv('MY_CHAT_ID', default='')
