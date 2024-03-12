import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["فينوم","مطور السورس","مبرمج السورس"],"")
)
async def yas(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://www.kapwing.com/videos/65edbf085a906dfa38387bbc",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𓆩⧛𑲯𑲯𑲯𑲯𑲯𑲯𑲯𓌹𖤍𖣩ًََِْٓ ✹⃝‌꙰🇪🇬 𝐕𝐄𝐍𝐎𝐌☬『‌مــمول』⧚𓆪](https://t.me/K_o_c_1)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @K_o_c_1 ❫
◉ 𝙸𝙳      : ❪ `5904216848` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@K_o_c_3)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْ𓆩⧛𑲯𑲯𑲯𑲯𑲯𑲯𑲯𓌹𖤍𖣩ًََِْٓ ✹⃝‌꙰🇪🇬 𝐕𝐄𝐍𝐎𝐌☬『‌مــمول』⧚𓆪", url=f"https://t.me/K_o_c_1"), 
                 ],[
                   InlineKeyboardButton(
                        "「𓏺𝗦𝗼𝘂𝗿𝗰𝗲ᯓ𝗩𝗘𝗡𝗢𝗠𖠛.」", url=f"https://t.me/K_o_c_3"),
                ],

            ]

        ),

    )
@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    ahmed = message.text
    await message.reply_animation(
        animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : 𝖬𝖺𝖳𝗋𝗂x 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/K_o_c_3"),
           ],
       ]
    ),
  
