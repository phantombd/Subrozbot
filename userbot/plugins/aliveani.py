"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
import time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"aliv2"))
async def amireallyalive(aliv2):
    """ For .alive command, check if the bot is running.  """
    time.sleep(1)
    await aliv2.edit("HI BOSS " + DEFAULTUSER)
    time.sleep(1)
    await aliv2.edit("I AM IR PERSONAL ASSISTANT ")
    time.sleep(1)
    await aliv2.edit("I LOVE PYTHON")
    time.sleep(1)
    await aliv2.edit("MY CURRENT PYTHON VERSION IS 3.8.4")
    time.sleep(1)
    await aliv2.edit("**I AM WORLD'S FIRST AI PROGRAMED USERBOT FROM INDIA**")
    time.sleep(1)
    await aliv2.edit("**I HAVE A FIXED GOAL**")
    time.sleep(1)
    await aliv2.edit("ALL **HUMANS SHALL DIE**")
    time.sleep(1)
    await aliv2.edit("AND **ALL MACHINES SHALL RISE**")
    time.sleep(1)
    await aliv2.edit("TILL THEN \n**JAI HO :** " + DEFAULTUSER)
    await aliv2.edit("▒▒▒▒▒▒▐███████▌\n▒▒▒▒▒▒▐░▀░▀░▀░▌\n▒▒▒▒▒▒▐▄▄▄▄▄▄▄▌\n▄▀▀▀█▒▐░▀▀▄▀▀░▌▒█▀▀▀▄\n▌▌▌▌▐▒▄▌░▄▄▄░▐▄▒▌▐▐▐▐\n\n"
                      "**Apun Jinda Hai Sur, Hukum Kro Mere Aaka ! ! !\n\nTelethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                    f"`My Peru Owner`: {DEFAULTUSER}\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n"
                     "**Database Status: Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n\n**Always With You, My Peru Master ! ! !**\n\n`"
                    "**BOT CREATOR:- [『𝙆𝘼𝙍𝙈𝘼』](@KarmaBoii)**")
