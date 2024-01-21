from DollXSpamBot import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from DollXSpamBot import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/a21ba38c03755bce23bb6.jpg"

DOLL_Help = "🗿 𝙇𝙪𝙘𝙠𝙮 ✘ 𝙎𝙥𝙖𝙢  🗿\n\n"

DOLL_Help = "**! 𝐋𝐔𝐂𝐊𝐘 𓆩⃟👑**\n"
 
DOLL_Help += f"𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 𝙄𝙉 𝙎𝙋𝘼𝙈 𝘽𝙊𝙏\n\n"

DOLL_Help += f" 𝙎𝙋𝘼𝙈 𝘽𝙊𝙏 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎\n\n"

DOLL_Help += f" `!ping` \n `!alive` , `!luck`  \n\n !`restart` \n\n `!addecho` \n\n `!rmecho`  \n\n `!addsudo` \n\n"
 
DOLL_Help += f"𝗕𝗔𝗖𝗞\n\n"

DOLL_Help += f" `!leave` \n\n"
 
DOLL_Help += f" 𝗦𝗣𝗔𝗠 𝗜𝗡𝗙𝗢\n\n"

DOLL_Help += f" `!raid`\n `!replyraid` \n\n `!dreplyraid`\n\n `!spam` \n `!bigspam` \n\n `!uspam`\n\n `!delayspam`\n\n"

DOLL_Help += f" `!pornspam` \n\n"

DOLL_Help += f" `!hang` \n\n"

DOLL_Help += f" `!bspam` \n\n"

DOLL_Help += f"@l1xky\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DOLL_Help)
