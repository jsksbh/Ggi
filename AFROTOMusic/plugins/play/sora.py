import asyncio

import random

from AFROTOMusic import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





txt = [


"تم اختيار لك هذه الصوره https://telegra.ph/file/c155afc7b6c3e91be379c.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/16d507492bb8008ae404d.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/7983df39d7921f81bb4d3.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/63b56b4d0e1db0ccb0741.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/2d15c66003a79cee2db63.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/49a56d946a59549f0c005.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/42aa387ab422669b9fd26.jpg",

        ]


        


@app.on_message(filters.command(["بوت","يا بوت"], ""))

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
