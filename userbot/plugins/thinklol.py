# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"lol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🤔🧐🤔🧐🤔🧐"))
	for _ in range(999):
		await asyncio.sleep(2)
		await event.edit("".join(deq))
		deq.rotate(1)
    
