import asyncio

import random

from AFROTOMusic import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





url = f"https://t.me/vnnkli/{rl}"


        


@app.on_message(filters.command(["صوره"," صورة"], ""))

async def khyrok(client: Client, message: Message):

      a = random.choice(rl)

      await message.reply(

        f"{a}")
