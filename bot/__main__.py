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

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot as app
from bot import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from bot.plugins import *
from pyrogram import idle, filters
from bot.plugins.Dev import *
from bot.helpers.fsub import fsub
from bot.helpers.database.add_user import AddUserToDatabase
from bot.helpers.fsub import ForceSub

BOT_USERNAME = "szsongbot"

START_TXT = """
Hello [{}](tg://user?id={}) 👋

I am **sz song Downloader Bot**

🎧You can download any song useing me
I can search song useing voice clip

If you want to know how to use me just
touch on `Help` Button 👨

☬─────────────☬
🤟 Bot Owner :- [Supun](https://t.me/supunmabot)
🦅 Powered By :- `【SZ™】`
☬─────────────☬


⚠️copyright ©️ 2021 [szteambots](https://t.me/szteambots). ** All Rights Reserved** 
"""

START_BTN = [
    [
        InlineKeyboardButton(text="Search on youtube here 🔎", switch_inline_query_current_chat="")
    ],
    [
        InlineKeyboardButton(text="Updates Channel🗣", url="https://t.me/szteambots"),
        InlineKeyboardButton(text=" Support Group👥", url="https://t.me/slbotzone"),
    ],
    [
        InlineKeyboardButton(text="🆘️ Help 🆘️",  callback_data="xelp")
    ],
    [
        InlineKeyboardButton(text="➕Add Me To Your Group➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),
    ],
]

@app.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await AddUserToDatabase(bot, update)    
    FSub = await ForceSub(bot, update)
    if FSub == 400:
        return
    await update.reply_photo(
        photo="https://telegra.ph/file/29710ffe0c70108ff1955.jpg",
        reply_markup=START_BTN,
        caption=START_TXT.format(name, user_id))
    )

app.start()
LOGGER.info("""
┏━┳┓╋╋╋╋╋┏┓╋╋╋┏┓┏┓╋╋┏┓
┃━┫┗┳━┓┏┳┫┗┳━┳┛┃┃┗┳━┫┗┓
┣━┃┏┫╋┗┫┏┫┏┫┻┫╋┃┃╋┃╋┃┏┫
┗━┻━┻━━┻┛┗━┻━┻━┛┗━┻━┻━┛
⚊❮❮❮❮  I am supun  ❯❯❯❯⚊
⚊❮❮❮❮  Join @sl_bot_zone ❯❯❯❯⚊
""")
idle()
