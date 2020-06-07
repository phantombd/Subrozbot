"""Emoji
Available Commands:
.np
Credits to @KarmaHacx
"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("np"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "np":
    await event.edit("np")
    animation_chars = [
            "No",
            "Problem",
            "Sir 😇",
            "No Problem Sir 😇",
            "No Problem Sir 😇. Jao",
            "No Problem Sir 😇. Jao enjoy",
            "No Problem Sir 😇. Jao enjoy karo"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
