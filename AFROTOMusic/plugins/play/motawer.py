import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from AFROTOMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["مطور البوت", "مطور", "المطور"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_video(
        video=f"https://telegra.ph/file/eebd6120a4ce4a2e75002.mp4",
        caption=f"""<b>» مرحبـاً بك عـزيـزي </b> {message.from_user.mention} .\n\n<b>» هذا هو حساب مطور البوت</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "ᯓ⭓𝙼𝚄𝚂𝙸𝙲✘𝚅𝙴𝙽𝙾𝙼♪𝅘𝅥𝅯•", url="https://t.me/K_o_c_3"),
                ],
            ]
        ),
    )
