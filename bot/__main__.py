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
from config import BOT_USERNAME
from bot.helpers.fsub import fsub


text = """
Hello [{}](tg://user?id={}) 👋

I am **Mayawee song bot**

😊Available Features 

Download  song 🎧
Download saavn 🎼
Download lyrics 📃
Download video  📥
If you want to know how to use me just
touch on `Help` Button 👨

☬─────────────☬
🤟 Bot Owner :- [Chathura](https://t.me/aboutchathura)
🦅 Powered By :- `【snt™】`
☬─────────────☬


⚠️copyright ©️ 2022 [Mayawee](https://t.me/Mayawee_bot_help). ** All Rights Reserved** 
"""

@app.on_message(filters.command("start"))
@fsub()
async def start(client, message): #fsub start
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        button = [
    [
        InlineKeyboardButton(text="Search on youtube here 🔎", switch_inline_query_current_chat="")
    ],
    [
        InlineKeyboardButton(text="Updates Channel🗣", url=""),
        InlineKeyboardButton(https://t.me/Mayawee_bot_help
            text=" Support Group👥", url="https://t.me/mayawee_songs"
        ),
    ],
    [
        InlineKeyboardButton(text="🆘️ Help 🆘️",  callback_data="xelp")
    ],
    [
        InlineKeyboardButton(text="➕Add Me To Your Group➕", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),
    ],
]
    else:
        button = None
    await message.reply_photo(
                    photo="https://telegra.ph/file/69d90dce171ee2ce2743a.jpg",
                    reply_markup=InlineKeyboardMarkup(button),
                    caption=text.format(name, user_id))



app.start()
LOGGER.info("""
┏━┳┓╋╋╋╋╋┏┓╋╋╋┏┓┏┓╋╋┏┓
┃━┫┗┳━┓┏┳┫┗┳━┳┛┃┃┗┳━┫┗┓
┣━┃┏┫╋┗┫┏┫┏┫┻┫╋┃┃╋┃╋┃┏┫
┗━┻━┻━━┻┛┗━┻━┻━┛┗━┻━┻━┛
⚊❮❮❮❮  Iamchathura   ❯❯❯❯⚊
⚊❮❮❮❮  Join @mayawee_songs ❯❯❯❯⚊
""")
idle()
