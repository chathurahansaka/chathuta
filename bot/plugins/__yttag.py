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


import os
from bot import bot as app

from pyrogram import Client, filters
import YoutubeTags
from YoutubeTags import videotags
rom pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery 

@app.on_message(filters.regex("https://www.youtube.com") | filters.regex("http://www.youtube.com") | filters.regex("https://youtu.be/") | filters.regex("https://www.youtu.be/") | filters.regex("http://www.youtu.be/"))
async def tag(bot, message):
    link = str(message.text)
    tags = videotags(link) 
    if tags=="":
         await message.reply_text(" `𝐍𝐨 𝐓𝐚𝐠𝐬 𝐅𝐨𝐮𝐧𝐝 🔖`")
    else:
         await message.reply_text(text=f"𝑺𝒆𝒍𝒆𝒄𝒕 𝒘𝒉𝒂𝒕 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒂𝒄𝒄𝒐𝒎𝒑𝒍𝒊𝒔𝒉 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏 𝒃𝒆𝒍𝒐𝒘 **\n\n𝓣𝓱𝓮𝓼𝓮 𝓪𝓻𝓮 𝓽𝓱𝓮 𝓽𝓪𝓰𝓼 𝓾𝓼𝓮𝓭 𝓯𝓸𝓻 𝓽𝓱𝓮 𝓿𝓲𝓭𝓮𝓸 𝔂𝓸𝓾 𝓼𝓮𝓷𝓽 𝓶𝓮\n\n\n ` {tags} ` \n\n\n 🔥 Pọwẹrẹɗ Ɓy : @SL_bot_zone\n\n☘️ 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 : @supunmabot",reply_markup=BUTTON)
 


BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝑺𝒍 𝑩𝒐𝒕 𝒁𝒐𝒏𝒆 ✍️", url=f"https://t.me/SL_bot_zone"),
                    InlineKeyboardButton("𝓢𝓛 𝓑𝓸𝓽 𝓒𝓱𝓪𝓽", url=f"https://t.me/slbotzone"),
                ],
                [
                    InlineKeyboardButton(text="📦 Socure Code 📦", url=f"https://github.com/youtubeslgeekshow/Youtube-tag-bot")],
            ]
        )
