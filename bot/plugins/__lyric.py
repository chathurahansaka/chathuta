import os
import requests
from bot import bot as app

from pyrogram import Client, filters


@app.on_message(filters.command(["lyric"))
async def lirik(_, message):
    rep = await message.reply_text("🔎 **searching lyrics...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("**give a lyric name too !**")
            return
        query = message.text.split(None, 1)[1]
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception as ex:
        print(ex)
        await rep.edit("**Lyrics not found.** please give a valid song name !")
