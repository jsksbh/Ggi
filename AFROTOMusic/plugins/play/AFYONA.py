import asyncio
from pyrogram import Client, filters
from strings.filters import command
from AFROTOMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️✨"




REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
         ("صوره")
    ],
    
    [
        ("العكس"),
        ("احرف")
    ],
    [
        ("مطور السورس"),
        ("مطور البوت")
    ],
   
    [
         ("كت"),
        ("صراحه")
    ],
    [
        ("❤استوري")
    ],
    [
        ("نكته"),
        ("كتابات")
    ],
    [
        ("اذكار"),
        ("قران") 
    ],
    [
         ("شعر"),
        ("انصحني")
    ],
    [
         ("احكام")
        
    ],
    [
        ("لو خيروك"),
         ("الالعاب")
    ],    
    [
        ("اخفاء الازرار")
    ]
  
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply("**تم قفل الكيبورد بنجاح**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يوتيوب"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://www12.0zz0.com/2024/03/07/17/197295459.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ S𝙾𝚞𝚁𝙲𝙴 V𝙴𝙽𝙾𝙼 𖠛", url=f"https://t.me/K_o_c_3"),
            ]
         ]
     )
  )

