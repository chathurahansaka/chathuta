import os
import asyncio
import time
import shlex
import requests
from typing import Tuple
from json import JSONDecodeError
from pyrogram import Client
from pyrogram.filters import command
from config import Config
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /find ` command again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/szteambots") 
        ]]      
    )

# ====== SHAZAM ======

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

async def fetch_audio(client, message):
    time.time()
    if not message.reply_to_message:
        await message.reply("`Reply To A Video / Audio.`")
        return
    warner_stark = message.reply_to_message
    if warner_stark.audio is None and warner_stark.video is None:
        await message.reply("`Format Not Supported`")
        return
    if warner_stark.video:
        lel = await message.reply("`Video Detected, Converting To Audio !`")
        warner_bros = await message.reply_to_message.download()
        stark_cmd = f"ffmpeg -i {warner_bros} -map 0:a friday.mp3"
        await runcmd(stark_cmd)
        final_warner = "friday.mp3"
    elif warner_stark.audio:
        lel = await edit_or_reply(message, "`Download Started !`")
        final_warner = await message.reply_to_message.download()
    await lel.edit("`Almost Done!`")
    await lel.delete()
    return final_warner


async def edit_or_reply(message, text, parse_mode="md"):
    if message.from_user.id:
        if message.reply_to_message:
            kk = message.reply_to_message.message_id
            return await message.reply_text(
                text, reply_to_message_id=kk, parse_mode=parse_mode
            )
        return await message.reply_text(text, parse_mode=parse_mode)
    return await message.edit(text, parse_mode=parse_mode)


@Client.on_message(command(["find", f"find@{Config.BOT_USERNAME}"]))
async def shazamm(client, message):
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return
    sz = await edit_or_reply(message, "**🔎 Searching your audio...**",disable_web_page_preview=True)
    if not message.reply_to_message:
        await sz.edit(f"👤Please **Reply To an Audio File** to find \nsong or use this format to find songs\n\n `/find alone` \n\n Need any Help [join updates channel](https://t.me/szteambots) or [supprt group](https://t.me/slbotzone) ")
        return
    if os.path.exists("friday.mp3"):
        os.remove("friday.mp3")
    kkk = await fetch_audio(client, message)
    downloaded_file_name = kkk
    f = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    await sz.edit("**Downloading Song... Please wait ⏰**")
    r = requests.post("https://starkapi.herokuapp.com/shazam/", files=f)
    try:
        xo = r.json()
    except JSONDecodeError:
        await sz.edit("`Seems Like Our Server Has Some Issues, Please Try Again Later!`")
        return
    if xo.get("success") is False:
        await sz.edit("❌ Found Nothing.\n\nTry another keywork or maybe spell it properly.")
        os.remove(downloaded_file_name)
        return
    button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Requested by🎧", url=f"https://t.me/{message.from_user.mention}")
        ],
        [
            InlineKeyboardButton("Support Chat 🔥️", url=f"https://t.me/slbotzone")
        ]
    ]
)   
    xoo = xo.get("response")
    zz = xoo[1]
    zzz = zz.get("track")
    zzz.get("sections")[3]
    nt = zzz.get("images")
    image = nt.get("coverarthq")
    by = zzz.get("subtitle")
    title = zzz.get("title")
    messageo = f"""<b>Found your song.</b>
🏷  Song Name : {title}
👁‍🗨 Song By : {by}
🎧 Requested by: {message.from_user.mention}
🤟 Identified Song: @szsongbot 
"""
    await client.send_photo(message.chat.id, image, messageo, reply_markup=button, parse_mode="HTML")
    os.remove(downloaded_file_name)
    await sz.delete()


