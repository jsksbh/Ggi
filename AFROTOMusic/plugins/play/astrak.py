from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from AFROTOMusic import app

channel = "K_o_c_3"
async def subscription(_, __: Client, message: Message):
    user_id = message.from_user.id
    try: await app.get_chat_member(channel, user_id)
    except UserNotParticipant: return False
    return True
    
subscribed = filters.create(subscription)

@app.on_message(~subscribed)
async def checker(_: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    user_id = message.from_user.id
    user = message.from_user.first_name
    markup = Markup([
        [Button("𓏺𝗦𝗼𝘂𝗿𝗰𝗲ᯓ𝗩𝗘𝗡𝗢𝗠𖠛", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"⛥┇‌ عذرًا عزيزي [ {user} ] \nٴ┄─━━━━━━━─┄\n⛥┇‌ عليك الإشتراك بقناة السورس أولا. ⚠️",
        reply_markup = markup
    )
    
