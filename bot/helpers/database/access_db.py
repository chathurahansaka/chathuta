import os
from config import Config
from helpers.database.database import Database

db = Database(Config.DATABASE_URL, Config.BOT_USERNAME)
