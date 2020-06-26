"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("▒▒▒▒▒▒▐███████▌\n▒▒▒▒▒▒▐░▀░▀░▀░▌\n▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌\n▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄\n▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐\n\n"
                      "**Apun Jinda Hai Sur, Hukum Kro Mere Aaka ! ! !\n\nTelethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                    f"`My Peru Owner`: {DEFAULTUSER}\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n\n**Always With You, My Peru Master ! ! !**\n\n"
                    "**BOT CREATOR:-** [『𝙆𝘼𝙍𝙈𝘼』](@KarmaBoii)")
