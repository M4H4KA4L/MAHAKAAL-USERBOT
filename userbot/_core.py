import asyncio
import os
from datetime import datetime
from pathlib import Path
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from mahakaalbot.utils import *
from userbot import *
from userbot import bot as mahakaalbot

DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Mahakaal User"
mahakaal_logo = "./MAHAKAAL/mahakaal_bot_logo.jpg"
Belongs_to_Lord_Shiva_nd_Haryana = mahakaalbot.uid
mahakaal = f"[{DEFAULTUSER}](tg://user?id={Belongs_to_Lord_Shiva_nd_Haryana})"

@mahakaalbot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@mahakaalbot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = mahakaal_logo
    input_str = event.pattern_match.group(1)
    omk = f"**⍟ Plugin name ≈** `{input_str}`\n**⍟ Uploaded by ≈** {mahakaal}\n\n⚡ **[ʟᴇɢᴇɴᴅᴀʀʏ ᴀғ ᴍᴀʜᴀᴋᴀᴀʟ ʙᴏᴛ](t.me/Official_MahakaalBot_Support)** ⚡"
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found..... Kek")

@mahakaalbot.on(admin_cmd(pattern="install$", outgoing=True))
@mahakaalbot.on(sudo_cmd(pattern="install$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    a = "__Installing.__"
    b = 1
    await event.edit(a)
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "./userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}` (sudo included)\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__Installing..__"
                            b = 2
                        else:
                            a = "__Installing...__"
                            b = 1
                        await event.edit(a)
                    return await event.edit(f"✅ **Installed module** :- `{shortname}` \n✨ BY :- {mahakaal}\n\n{string}\n\n        ⚡ **[ʟᴇɢᴇɴᴅᴀʀʏ ᴀғ ᴍᴀʜᴀᴋᴀᴀʟ ʙᴏᴛ](t.me/Official_MahakaalBot_Support)** ⚡", link_preview=False)
                return await event.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await event.edit(f"**Failed to Install** \n`Error`\nModule already installed or unknown format")
        except Exception as e: 
            await event.edit(f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)
    
@mahakaalbot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@mahakaalbot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def uninstall(Belongs_to_Lord_Shiva_nd_Haryana):
    if Belongs_to_Lord_Shiva_nd_Haryana.fwd_from:
        return
    shortname = Belongs_to_Lord_Shiva_nd_Haryana.pattern_match["shortname"]
    dir_path =f"./userbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await Belongs_to_Lord_Shiva_nd_Haryana.edit(f"Uninstalled `{shortname}` successfully")
    except OSError as e:
        await Belongs_to_Lord_Shiva_nd_Haryana.edit("Error: %s : %s" % (dir_path, e.strerror))

@mahakaalbot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@mahakaalbot.on(sudo_cmd(pattern=r"upload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded `{shortname}`")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@mahakaalbot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@mahakaalbot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )

CmdHelp("core").add_command(
  "install", "<reply to a .py file>", "Installs the replied python file if suitable to userbot codes. (TEMPORARILY DISABLED AS HACKERS MAKE YOU INSTALL SOME PLUGINS AND GET YOUR DATA)"
).add_command(
  "uninstall", "<plugin name>", "Uninstalls the given plugin from userbot. To get that again do .restart", "uninstall alive"
).add_command(
  "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
  "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
  "send", "<file name>", "Sends the given file from your userbot server, if any.", "send alive"
).add_command(
  "cmds", None, "Gives out the list of modules in mahakaalbot."
).add()
