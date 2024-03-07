import asyncio
from pyrogram import Client, filters
from AFROTOMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.regex("^ايدي$") & filters.group & SUDOERS)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""**↯ : وفي النهاية أنتم السيئون وهم الأبرياء**
            
**↯ : اسمك : › {message.from_user.mention}**
                    
**↯ : معرفك : › @{message.from_user.username}**
                    
**↯ : ايديك : › `{message.from_user.id}`**
                    
**↯ : النبذه : › \n {bio}**""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                                            name, user_id=5904216848)
                ],

            ]

        ),

    )
    
    
