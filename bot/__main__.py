#youtubeslgeekshow
#fsub my channel only

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import bot as app
from bot import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied #fsub
from bot.plugins import *
from pyrogram import idle, filters

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/sl_bot_zone") 
        ]]      
    )

text = """
Hello [{}](tg://user?id={}) 👋

If you want to know how to use this bot just
touch on " Help "  Button 👨
"""

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
                text="Help & commands 🛠", callback_data="bot_commands"
            ),
            InlineKeyboardButton(
                text="Developers ✨",
                url="https://github.com/thehamkercat/WilliamButcherBot",
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
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
    ]
)

    else:
        button = None
    await message.reply(text.format(name, user_id), reply_markup=button)

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "group":
        Button = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Updates Channel🗣", url="https://t.me/SL_bot_zone"
                    ),
                    InlineKeyboardButton(
                        text="Support Chat 💭", url="https://t.me/slbotzone"
                    )
                ]
            ]
        )

    else:
        button = None
    await message.reply(Text.format(name, user_id), reply_markup=Button)

app.start()
LOGGER.info("𝖄𝖊𝖘 𝕴'𝖒 𝖆𝖑𝖎𝖛𝖊 🤭")
idle()
