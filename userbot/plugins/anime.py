import re

from mahakaalbot import bot
from mahakaalbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from mahakaalbot.cmdhelp import CmdHelp
from mahakaalbot.helpers.functions import deEmojify
from userbot.Config import Config
from . import *

@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(Belongs_to_Lord_Shiva_nd_Haryana):
    mahakaal = Belongs_to_Lord_Shiva_nd_Haryana.pattern_match.group(1)
    if not mahakaal:
        if Belongs_to_Lord_Shiva_nd_Haryana.is_reply:
            (await Belongs_to_Lord_Shiva_nd_Haryana.get_reply_message()).message
        else:
            await edit_or_reply(Belongs_to_Lord_Shiva_nd_Haryana, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(mahakaal))}")

    await troll[0].click(
        Belongs_to_Lord_Shiva_nd_Haryana.chat_id,
        reply_to=Belongs_to_Lord_Shiva_nd_Haryana.reply_to_msg_id,
        silent=True if Belongs_to_Lord_Shiva_nd_Haryana.is_reply else False,
        hide_via=True,
    )
    await Belongs_to_Lord_Shiva_nd_Haryana.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
