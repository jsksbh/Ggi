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
"تم اختيار لك هذه الصوره https://telegra.ph/file/e348106d5d91c8ba0f5a2.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/2edf7ddcb30f565bb8783.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/226de07b9cd0858ca45a6.jpg", 
"تم اختيار لك هذه الصوره https://telegra.ph/file/26048e69dc14f8308278a.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/22ab9ef383b082c931ed9.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/a84299faed47ec848e814.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/a51ba9e89034ae5eb58a9.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/c931864e5787b503acbcb.jpg",
"تم اختيار لك هذه الصوره https://telegra.ph/file/c9311fb1095b53f49e707.jpg",  
"تم اختيار لك هذه الصوره https://telegra.ph/file/37b7e54cc65e35bb2152a.jpg",  
"تم اختيار لك هذه الصوره https://telegra.ph/file/7bc310a52e71bdbd0143c.jpg", 
  "تم اختيار لك هذه الصوره https://telegra.ph/file/45b557af4d2f388ad8272.jpg",





]


        


@app.on_message(filters.command(["صوره","صورة"], ""))

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
