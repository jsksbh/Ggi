from pyrogram import Client, filters
from pyrogram.types import Message
import requests 
from AFROTOMusic import app

muted = []
@app.on_message(filters.command("كتم", "") & filters.group)
async def ktm(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        memberB = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if memberB["result"]["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك كتم مشرف او مالك", reply_to_message_id=message.message_id)
            if message.reply_to_message.from_user.id in muted: return await message.reply("- هذا المستخدم مكتوم!")
            muted.append(message.reply_to_message.from_user.id)
            await message.reply_text(f"تم كتم  العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        elif member["result"]["status"] == "creator":
            if message.reply_to_message.from_user.id in muted: return await message.reply("- هذا المستخدم مكتوم!")
            muted.append(message.reply_to_message.from_user.id)
            await message.reply_text(f"تم كتم  العضو\n│ \n└ʙʏ : {message.reply_to_message.from_user.mention}\n\n بنجاح ")
            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.message_id)


@app.on_message(filters.command("الغاء كتم", "") & filters.group)
async def unktm(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if message.reply_to_message.from_user.id not in muted: return await message.reply("- هذا المستخدم غير مكتوم!")
            muted.remove(message.reply_to_message.from_user.id)
            await message.reply_text(f"تم الغاء  العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        elif member["result"]["status"] == "creator":
            if message.reply_to_message.from_user.id not in muted: return await message.reply("- هذا المستخدم غير مكتوم!")
            muted.remove(message.reply_to_message.from_user.id)
            await message.reply_text(f"تم الغاء  العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.message_id)


@app.on_message(filters.command("المكتومين", ""))
async def maktom(_: Client, message: Message):
    if not len(muted): return await message.reply("- لا يوجد مكتومين!")
    names = "\n".join(["- " + (await app.get_chat(id)).first_name for id in muted])
    caption = f"- المكتومين: \n\n{names}"
    await message.reply(caption, reply_to_message_id=message.message_id)


@app.on_message(filters.command("مسح المكتومين", ""))
async def ms7maktom(_: Client, message: Message):
    member = member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
    if member["result"]["status"] not in ["creator", "administrator"]: return await message.reply_text(f"يجب ان تكون ادمن علي الاقل لاستخدام هذا الامر\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")
        
    if not len(muted): return await message.reply("- لا يوجد مكتومين لحذفهم!")
    muted.clear()
    await message.reply_text(f"تم مسح المكتومين \n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

    

@app.on_message(filters.text & filters.group, group=928)
async def ktmf(_: Client, message: Message):
    if message.from_user.id in muted: await message.delete()
    

@app.on_message(filters.command("طرد", "") & filters.group)
async def tard(_: Client, message: Message):
    if message.reply_to_message:
        member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.from_user.id}").json()
        memberB = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={message.chat.id}&user_id={message.reply_to_message.from_user.id}").json()
        if member["result"]["status"] == "administrator":
            if memberB["result"]["status"] in ["creator", "administrator"]:return await message.reply("- لا يمكنك طرد مشرف او مالك", reply_to_message_id=message.message_id)
            try:await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            except: return await message.reply_text(f"ليس لدي صلاحيات لطرد هذا العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            await message.reply_text(f"تم طرد العضو \n│ \n : {message.reply_to_message.from_user.mention}\n\n بنجاح ")

            return
        elif member["result"]["status"] == "creator":
            try:await app.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            except: return await message.reply_text(f"ليس لدي صلاحيات لطرد العضو\n│ \n : {message.reply_to_message.from_user.mention}\n\n  بنجاح")

            await message.reply("- تم طرد العضو بنجاح!", reply_to_message_id=message.message_id)
            return
     else: await message.reply("- يجب ان تكون ادمن على الاقل لإستخدام هذا الامر.", reply_to_message_id=message.message_id)

@app.on_message(filters.command(["الغاء حظر"]))
def unban_users(client, message):
    # Check if the user is an admin
    if message.from_user.id == message.chat.id:
        # Check if the message has user IDs
        if len(message.command) > 1:
            user_ids = message.command[1:]
            for user_id in user_ids:
                # Unban the user
                client.unban_chat_member(message.chat.id, int(user_id))
                message.reply(f"User {user_id} has been unbanned successfully!")
        else:
            message.reply("Please specify user IDs to unban.")
    else:
        message.reply("You are not authorized to perform this action.")


    
