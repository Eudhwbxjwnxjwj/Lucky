
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DollXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DOLL_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/9dbf83e586fdf5c60be73.jpg"



        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"@l1xky''
        DOLL_ON = f"""
𝗛𝗘𝗬 {mention},
𝗟𝗨𝗖𝗞𝗬𝗫𝗦𝗣𝗔𝗠 𝗕𝗢𝗧 𝗛𝗘𝗥𝗘\n~ @l1xky
    """
        await e.client.send_file(e.chat_id, DOLL_IMG, caption=DOLL_ON)
