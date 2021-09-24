from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot as app
from bot import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied #fsub
from bot.plugins import *
from pyrogram import idle, filters
from bot.plugins.Dev import *


JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/sl_bot_zone") 
        ]]      
    )

text = """
Hello [{}](tg://user?id={}) 👋
I am advance song downloader bot
With more features!😊
If you want to know how to use this bot just
touch on `Help` Button 👨
"""
botton = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Updates", url ="https://t.me/szroseupdates")]],
     )
@app.on_message(filters.command("start"))
async def start(client, message): #fsub start
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return   #fsub end
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
            button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Help & commands 🛠", callback_data="help"
            ),
            InlineKeyboardButton(
                text="Developers ✨",
                callback_data="dev",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Updates Channel🗣",
                url ="https://t.me/SL_bot_zone",
            ),
            InlineKeyboardButton(
                text="Support Group👥", url="https://t.me/slbotzone"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Add Me To Your Group 🎉",
                url=f"http://t.me/szrosebot?startgroup=new",
            )
        ],
    ]      
 )
          await message.reply_photo[
                    photo="https://telegra.ph/file/1804aa067b165793c6a1a.jpg",
                    reply_markup=button,
                    caption=text.format(name, user_id)]
    else:
         await message.reply_text("I am now online ")
app.start()
LOGGER.info("""
┏━┳┓╋╋╋╋╋┏┓╋╋╋┏┓┏┓╋╋┏┓
┃━┫┗┳━┓┏┳┫┗┳━┳┛┃┃┗┳━┫┗┓
┣━┃┏┫╋┗┫┏┫┏┫┻┫╋┃┃╋┃╋┃┏┫
┗━┻━┻━━┻┛┗━┻━┻━┛┗━┻━┻━┛
⚊❮❮❮❮  I am supun  ❯❯❯❯⚊
⚊❮❮❮❮  Join @sl_bot_zone ❯❯❯❯⚊
""")
idle(
