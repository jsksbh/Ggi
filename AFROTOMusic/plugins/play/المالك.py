import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



@zohary.on_message(filters.command(["المالك"],""))
async def creator(c,msg):
    x = []
    async for m in zohary.get_chat_members(msg.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       lol = await zohary.get_users(int(x[0]))
       if lol.photo:
         async for photo in zohary.get_chat_photos(x[0],limit=1):
          await msg.reply_photo(photo.file_id,caption=f"ΌᎳΝᎬᎡ | - {lol.mention} 🕷",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(lol.first_name, url=f"https://t.me/{lol.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await msg.reply_text(f"ΌᎳΝᎬᎡ | - {lol.mention} 🕷", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(lol.first_name, url=f"https://t.me/{lol.username}")],]))
    else:
        await msg.reply_text("الاك محذوف يقلب")
