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

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

from bot import bot as app

#song text
TEXT = "🌟Use Bellow Format \n\n💫 Format :- /song <song name >"
#lyric text
LYRIC = "🌟Use Bellow Format \n\n💫 Format :- /lyric <lyric name >"
#Video Download text
VIDEO = "🌟Use Bellow Format \n\n💫 Format :- /video <video name >"
#saavn  text
SAAVN = "🌟Use Bellow Format \n\n💫 Format :- /saavn <saavn name >"

@app.on_callback_query(filters.regex("help"))
async def help(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Help menu off szsong bot
""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Song Download", callback_data="songback")
                ],[
                    InlineKeyboardButton(
                        "lyric Download", callback_data="lyricback")
                ],[
                    InlineKeyboardButton(
                        "Video Download", callback_data="videoback")
                ],[
                    InlineKeyboardButton(
                        "saavn Download ", callback_data="saavnback"
                    )
                ],[
                     InlineKeyboardButton(
                        "About", callback_data="about"
                    )
                ],[
                     InlineKeyboardButton(
                        "Search Inline🔎 ", switch_inline_query_current_chat=""
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
    
@app.on_callback_query(filters.regex("lyricback"))
async def lyric_callbacc(_, CallbackQuery):
    text = LYRIC
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)     
    
@app.on_callback_query(filters.regex("videoback"))
async def video_callbacc(_, CallbackQuery):
    text = VIDEO
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)   

@app.on_callback_query(filters.regex("saavnback"))
async def saavn_callbacc(_, CallbackQuery):
    text = SAAVN
    await app.answer_callback_query(CallbackQuery.id, text, show_alert=True)  
    
@app.on_callback_query(filters.regex("about"))
async def about(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""About menu
""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "About Bot🤖", callback_data="botback")
                ],[
                    InlineKeyboardButton(
                        "About Developers ", callback_data="devback")
                ],[
                    InlineKeyboardButton(
                        "About You", callback_data="youback")
                ],[
                    InlineKeyboardButton(
                        "About szrose", callback_data="roseback"
                    )
                ],[
                     InlineKeyboardButton(
                        "Help Menu", callback_data="help"
                    )
                ],[
                     InlineKeyboardButton(
                        "Close", callback_data="cls"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )     
@app.on_callback_query(filters.regex("botback"))
async def botback(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ Bot :  Song Downloader Bot (https://t.me/szrosebot)
✨ Developer : szbots 🇱🇰 (https://telegram.me/sl_bot_zone)
✨ Updates Channel :  Updates (https://telegram.me/sl_bot_zone)
✨ Support Group : Support (https://telegram.me/slbotzone)
✨ Language : Python3 (https://python.org/)
✨ Library : Pyrogram (https://pyrogram.org/)
✨ Hosting service : Heroku (https://www.heroku.com/)
""",
        reply_markup=InlineKeyboardMarkup(
            [ 
               [
                     InlineKeyboardButton(
                        "Help", callback_data="help"
                    )
                ],[
                     InlineKeyboardButton(
                        "Back", callback_data="about"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )  
