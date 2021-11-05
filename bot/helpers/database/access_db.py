import os
from bot.helpers.database.database import Database
from config import Config

BOT_USERNAME = "szsongbot"

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
