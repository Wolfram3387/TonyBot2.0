import os
import logging

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URI = os.getenv("URI")
IP = os.getenv("ip")
ADMINS = [868136575]

logging.basicConfig(level=logging.INFO)


aiogram_redis = {
    'host': IP,
}
redis = {
    'address': (IP, 6379),
    'encoding': 'utf8'
}
