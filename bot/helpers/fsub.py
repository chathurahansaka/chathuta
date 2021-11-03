from functools import wraps
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def fsub():
    def fsubfunc(func):
        @wraps(func)
        async def checkfsub(_, message, *args, **kwargs):
            try:
                await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
            except UserNotParticipant:
               return await message.reply_text(
        text=" **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊", disable_web_page_preview=True, 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Join our update Channel 🗣", url="https://t.me/szteambots") ]]))
            return await func(_, message, *args, **kwargs)
        return checkfsub
    return fsubfunc
