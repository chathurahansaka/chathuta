#MIT License

#Copyright (c) 2021 slgeekshow

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.



import sys
import os
import heroku3
import time
import traceback
import asyncio
import shutil
import psutil
import motor

from telethon import TelegramClient
from telethon import events
from pyrogram import Client, filters
from pyrogram.types import Message, Dialog, Chat
from pyrogram.errors import UserAlreadyParticipant
from datetime import datetime
from functools import wraps
from os import environ, execle, path, remove

from bot import bot as app
from bot.helpers.database import db
from bot.helpers.dbthings import main_broadcast_handler
from bot.helpers.humanbytes import humanbytes
from config import BOT_USERNAME, BOT_OWNER, HEROKU_URL, HEROKU_API_KEY, HEROKU_APP_NAME, SUDO_USERS

heroku_api = "https://api.heroku.com"
Heroku = heroku3.from_key(HEROKU_API_KEY)

# Stats Of  Bot
@app.on_message(filters.command("stats"))
async def botstats(_, message: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await message.reply_text(
        text=f"**💫 Bot Stats Of @{BOT_USERNAME} 💫** \n\n**🤖 Bot Version:** `V2.9.1` \n\n**👥 Users:** \n ↳**PM'ed Users:** `{total_users}` \n\n**💾 Disk Usage,** \n ↳**Total Disk Space:** `{total}` \n ↳**Used:** `{used}({disk_usage}%)` \n ↳**Free:** `{free}` \n\n**🎛 Hardware Usage,** \n ↳**CPU Usage:** `{cpu_usage}%` \n ↳**RAM Usage:** `{ram_usage}%`",
        parse_mode="Markdown",
        quote=True
    )


# Broadcast message to users (This will Broadcast using Bot with Db)
@app.on_message(filters.private & filters.command("broadcast") & filters.user(BOT_OWNER) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)


# Ban User
@app.on_message(filters.private & filters.command("ban") & filters.user(BOT_OWNER))
async def ban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban Users from using this bot 🤒! Read __**/modhelp**__ to Learn how to use this 🤭!",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = ' '.join(m.command[3:])
        ban_log_text = f"`Banning User 🗑...` \nUser ID: `{user_id}` \nDuration: `{ban_duration}` \nReason: `{ban_reason}`"
        try:
            await c.send_message(
                user_id,
                f"Lmao You are **Banned 😂!** \n\nReason: `{ban_reason}` \nDuration: `{ban_duration}` day(s). \n\n**Message From The Owner! Ask in **@Nexa_bots** if you think this was an mistake."
            )
            ban_log_text += '\n\nSuccessfully Notified About This Ban to that **Dumb User** 😅'
        except:
            traceback.print_exc()
            ban_log_text += f"\n\nKCUF! I can't Notify About This Ban to That **Dumb User** 🤯 \n\n`{traceback.format_exc()}`"
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(
            ban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"An Error Occoured ❌! Traceback is given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


# Unban User
@app.on_message(filters.private & filters.command("unban") & filters.user(BOT_OWNER))
async def unban(c: Client, m: Message):
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban Users from using this bot 🤒! Read __**/modhelp**__ to Learn how to use this 🤭!",
            quote=True
        )
        return
    try:
        user_id = int(m.command[1])
        unban_log_text = f"`Unbanning user...` /n**User ID:**{user_id}"
        try:
            await c.send_message(
                user_id,
                f"Good News! **You are Unbanned** 😊!"
            )
            unban_log_text += '\n\nSuccessfully Notified About This to that **Good User** 😅'
        except:
            traceback.print_exc()
            unban_log_text += f"\n\nKCUF! I can't Notify About This to That **Dumb User** 🤯 \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(
            unban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"An Error Occoured ❌! Traceback is given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


# Banned User List
@app.on_message(filters.private & filters.command("banlist") & filters.user(BOT_OWNER))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ''
    async for banned_user in all_banned_users:
        user_id = banned_user['id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"➬ **User ID**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned Date**: `{banned_on}`, **Ban Reason**: `{ban_reason}`\n\n"
    reply_text = f"**Total Banned:** `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-user-list.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-user-list.txt', True)
        os.remove('banned-user-list.txt')
        return
    await m.reply_text(reply_text, True)



# set heroku vers
@app.on(events.NewMessage(pattern="^/(set|see|del) var(?: |$)(.*)(?: |$)([\s\S]*)")
async def variable(event):
    if event.fwd_from:
        return
    if event.sender_id == SUDO_USERS:
        pass
    else:
        return
    """
    Manage most of ConfigVars setting, set new var, get current var,
    or delete var...
    """
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        return await event.reply("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = event.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "see":
        k = await event.reply("`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            variable = event.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await k.edit(
                    "**ConfigVars**:" f"\n\n`{variable} = {heroku_var[variable]}`\n"
                )
            else:
                return await k.edit(
                    "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await event.client.send_file(
                        event.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await k.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        s = await event.reply("`Setting information...weit ser`")
        variable = event.pattern_match.group(2)
        if not variable:
            return await s.edit(">`.set var <ConfigVars-name> <value>`")
        value = event.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = event.pattern_match.group(2).split()[1]
            except IndexError:
                return await s.edit(">`/set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await s.edit(
                f"**{variable}**  `successfully changed to`  ->  **{value}**"
            )
        else:
            await s.edit(
                f"**{variable}**  `successfully added with value`  ->  **{value}**"
            )
        heroku_var[variable] = value
    elif exe == "del":
        m = await event.edit("`Getting information to deleting variable...`")
        try:
            variable = event.pattern_match.group(2).split()[0]
        except IndexError:
            return await m.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await m.edit(f"**{variable}**  `successfully deleted`")
            del heroku_var[variable]
        else:
            return await m.edit(f"**{variable}**  `is not exists`")
        

# Restart Your Bot
@app.on_message(filters.command("restart") & filters.user(BOT_OWNER))
async def restart(client: Client, message: Message, hap):
    msg = await message.reply_text("`Restarting Now! Please wait...`")
    hap.restart()
