import os
import pytube
from pyrogram import filters
from bot import bot

@bot.on_message(filters.command(['nsong']))
async def sendsong(_, message):
    link =  pytube.YouTube('https://youtu.be/9bZkp7q19f0')
    song = link.streams.filter(only_audio=True).first()
    down = song.download()
    base, ext = os.path.splitext(down)
    new_file = base + '.mp3'
    os.rename(down, new_file)
    await message.reply_audio(new_file)
    if os.path.exists(new_file):
            os.remove(new_file)
