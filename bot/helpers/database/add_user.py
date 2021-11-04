import os
from helpers.database.access_db import db
from pyrogram import Client
from config import Config
from pyrogram.types import Message

async def AddUserToDatabase(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"**🔔 News ** #NEW_USER: \n@szsongbot **Started To Using Me** \n\nFirst Name: `{message.from_user.first_name}` \nUser ID: `{message.from_user.id}` \nuser link : [{message.from_user.first_name}](tg://user?id={message.from_user.id})\nusername : {message.from_user.username}""
            )
