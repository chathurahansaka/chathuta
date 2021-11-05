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
import requests
from bot import bot as app

from pyrogram import Client, filters


@app.on_message(filters.command(["lyrics"]))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **searching your lyrics...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**give a lyric name too !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"🎼 **lyrics  search Successfully**✅\n\n◇───────────────◇ `{resp['data']}´\n\n◇───────────────◇\n\n🔥**Downloaded by**:@szsongbot  \n🌷 **Requestor** : {message.from_user.username}\n⚡️ **Powered By**   : 【SZ™】\n\©2021【SZ™】 team  **All Right Reserved**⚠️️   "
        await message.reply_photo(
                                  photo = "https://telegra.ph/file/376c689344b00516216d0.jpg",
                                  caption = result,
                                  disable_web_page_preview=True)
        await rep.delete()
    except Exception as ex:
        print(ex)
        await rep.edit("**Lyrics not found.** please give a valid song name !")
