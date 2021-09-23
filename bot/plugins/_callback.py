#youtubeslgeekshow

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from bot import bot as app

#song text
TEXT = "🌟Use Bellow Format \n\n💫 Format :- /song <song name >"


@app.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Help menu off szsong bot
""",
        reply_markup=InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton(
                         "Song Download", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "lyric Download", callback_data="cbcmds")
                ],[
                    InlineKeyboardButton(
                        "Video Download", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "saavn Download ", callback_data="cbcmds")
                 ],[
                    InlineKeyboardButton(
                        "Next", callback_data="cbcmds"
                    )
                  ]
           ]
        ),
     disable_web_page_preview=True
    )
@app.on_callback_query(filters.regex("songback"))
async def song_callbacc(_, CallbackQuery):
    text = TEXT
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)           
    
    
