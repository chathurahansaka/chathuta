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

    
@app.on_callback_query(filters.regex("about"))
async def about(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""
✨ Bot :  [Song Downloader Bot](https://t.me/szsongbot)
✨ Owner : [supunmabot](https://telegram.me/supunmabot)
✨ Updates Channel :  [Updates ](https://telegram.me/szteambots)
✨ Support Group : [Support ](https://telegram.me/slbotzone)
✨ Language : [Python3 ](https://python.org/)
✨ Library : [Pyrogram ](https://pyrogram.org/)
✨ Hosting service : [Heroku ](https://www.heroku.com/)
""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                     InlineKeyboardButton(
                        "🗑Close🗑", callback_data="cls"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )  

button = InlineKeyboardMarkup(
            [ 
                [       
                     InlineKeyboardButton("🎭 About Bot", callback_data="about")
                ],
                [
                     InlineKeyboardButton( "🗑Close🗑 ", callback_data="cls")
                ]
            ]
        )
    

@app.on_message(filters.command("help"))
async def help(client, message):
    text = f"""
Hello {message.from_user.mention} 👋 This is szsongbot Help menu
Use Bellow Format to get song / video / lyric / saavn 

✮ /song song name

✮ /lyric lyric name 

✮ /video video name

✮ /saavn saavn name 

☬─────────────☬
🤟 Bot Owner :- [supun](https://t.me/supunmabot)
🦅 Powered By :- `【SZ™】`
☬─────────────☬

⚠️copyright ©️ 2021 [szteambots](https://t.me/szteambots). ** All Rights Reserved** 
"""   
    await message.reply_photo(
                    photo=f"https://telegra.ph/file/d811f0125cb6cc5932780.jpg",
                    reply_markup=button,
                    caption=text)


@app.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

@app.on_callback_query(filters.regex("xelp"))
async def xelp(_, query: CallbackQuery):
    await query.edit_message_text(
         f"""
Hello {message.from_user.mention} 👋 This is szsongbot Help menu
Use Bellow Format to get song / video / lyric / saavn 

✮ /song song name 

✮ /lyric lyric name

✮ /video video name 

✮ /saavn saavn name 

☬─────────────☬
🤟 Bot Owner :- [supun](https://t.me/supunmabot)
🦅 Powered By :- `【SZ™】`
☬─────────────☬

⚠️copyright ©️ 2021 [szteambots](https://t.me/szteambots). ** All Rights Reserved** 
""",
       reply_markup = InlineKeyboardMarkup(
            [ 
                [       
                     InlineKeyboardButton("🎭 About Bot", callback_data="about")
                ],
                [
                     InlineKeyboardButton( "🗑Close🗑 ", callback_data="cls")
                ]
            ]
        ),
      disable_web_page_preview=True
    )  


