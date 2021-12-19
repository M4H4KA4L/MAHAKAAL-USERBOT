
# Thanks to @D3_krish
# Porting in MahakaalBot by @Belongs_to_Lord_Shiva_nd_Haryana

import asyncio
import random
from telethon import events, version
from userbot import mahakaalversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ᴍᴀʜᴀᴋᴀᴀʟʙᴏᴛ"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mahakaal = bot.uid

MAHAKAAL_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/4867a82215dd55270c85a.mp4"
pm_caption = "  __**💝💝 𝐌𝐀𝐇𝐀𝐊𝐀𝐀𝐋 𝐈𝐒 𝐒𝐓𝐈𝐋𝐋 𝐀𝐋𝐈𝐕𝐄 💝💝**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n  **『😈[{DEFAULTUSER}](tg://user?id={mahakaal})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•❥︎➼❥︎ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•❥︎➼❥︎ `Version:` `{mahakaalversion}`\n"
pm_caption += f"┣•❥︎➼❥︎ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•❥︎➼❥︎ `Channel:` [𝐉𝐎𝐈𝐍](https://t.me/Official_MahakaalBot_Support)\n"
pm_caption += f"┣•❥︎➼❥︎ `Creator:` [𝑴𝒂𝒉𝒂𝒌𝒂𝒂𝒍](https://t.me/Belongs_to_Lord_Shiva_nd_Haryana)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥REPO🔥](https://github.com/M4H4KA4L/MAHAKAALBOT) 🔹 [📜License📜](https://github.com/M4H4KA4L/MAHAKAALBOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAHAKAAL_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
