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
from pyrogram.errors import UserNotParticipant
from bot.plugins import *
from pyrogram import idle, filters
from config import BOT_USERNAME, photo
from helpers.commands import show_status_count

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/szteambots") 
        ]]      
    )

@app.on_message(filters.command('[start]'))
async def start(client, message): #fsub start
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return   #fsub end
    text = f"""
Hello {message.from_user.mention} 👋

I am sz song Downloader Bot
You can download any song useing me
I can search song useing voice clip

If you want to know how to use me just
touch on `Help` Button 👨

☬─────────────☬
🤟 Bot Owner :- [IMkashyapaa ](https://t.me/IMkashyapaa)
🦅 Powered By :- `【SZ™】`
☬─────────────☬

⚠️copyright ©️ 2021 [szteambots](https://t.me/szteambots). ** All Rights Reserved** 
"""   
    await message.reply_photo(
                    photo=f"{photo}",
                    reply_markup=InlineKeyboardMarkup(button),
                    caption=text)
button = [
    [
        InlineKeyboardButton(text="Bot Owner 🤟",  url="https://t.me/IMkashyapaa"),
        InlineKeyboardButton(
            text="Bot's statistics✨", callback_data="stat_callback"
        ),
    ],
    [
        InlineKeyboardButton(text="Updates Channel🗣", url="https://t.me/szteambots"),
        InlineKeyboardButton(
            text=" Support Group👥", url="https://t.me/slbotzone"
        ),
    ],
    [
        InlineKeyboardButton(text="Help",  callback_data="help")
    ],
    [
        InlineKeyboardButton(text="Add Me To Your Group 🎉", url=f"http://t.me/{BOT_USERNAME}?startgroup=new"),
    ],
]

@app.on_callback_query(filters.regex("stat_callback"))
async def stat_callbacc(_, CallbackQuery):
    text = await show_status_count
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)            



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
