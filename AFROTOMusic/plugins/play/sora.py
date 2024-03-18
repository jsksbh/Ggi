import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AFROTOMusic import app
import random
    

@app.on_message(command([f"صوره", "صورة", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/YVb_hbs/{rl}"
    await client.send_photo(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الصوره لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )

@app.on_message(command([f"❤استوريهات", "استوري"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/HH_bva/{rl}"
    await client.send_audio(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاستوري  لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
    
