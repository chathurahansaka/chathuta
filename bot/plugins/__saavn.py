from bot import bot
from bot import ARQ_API_KEY
from pyrogram import filters
from Python_ARQ import ARQ
from aiohttp import ClientSession
from io import BytesIO

is_downloading = False
ARQ_API_URL = "https://thearq.tech"
session = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

# Funtion To Download Song
async def download_song(url):
    async with session.get(url) as resp:
        song = await resp.read()
    song = BytesIO(song)
    song.name = "a.mp3"
    return song

@bot.on_message(filters.command("saavn") & ~filters.edited)
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        return await message.reply_text("/saavn requires an argument.")
    if is_downloading:
        return await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
    is_downloading = True
    text = message.text.split(None, 1)[1]
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.saavn(text)
        if not songs.ok:
            await m.edit(songs.result)
            is_downloading = False
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        sduration = songs.result[0].duration
        await m.edit("Downloading")
        song = await download_song(slink)
        await m.edit("Uploading")
        await message.reply_audio(
            audio=song,
            title=sname,
            performer=ssingers,
            duration=sduration,
        )
        await m.delete()
    except Exception as e:
        is_downloading = False
        return await m.edit(str(e))
    is_downloading = False
    song.close()
