import os
from bot.helpers.database.database import Database
from configs import Config

BOT_USERNAME = "szsongbot"

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
