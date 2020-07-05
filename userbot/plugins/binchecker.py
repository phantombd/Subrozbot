# © KarmaBot
# Created by @Karmaboii

import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
import time
from userbot import ALIVE_NAME

naam = str(ALIVE_NAME)


bot = "@uNiqueko_bot"

@borg.on(admin_cmd("bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!bin")
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!bin " + sysarg)
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")

@borg.on(admin_cmd("chk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!chk")
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!chk " + sysarg)
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")

@borg.on(admin_cmd("pp ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!pp")
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!pp " + sysarg)
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")

@borg.on(admin_cmd("ccn ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!ccn")
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!ccn " + sysarg)
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")

@borg.on(admin_cmd("csk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!csk")
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!csk " + sysarg)
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")

@borg.on(admin_cmd("cid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!cid")
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")
    elif "" in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("!cid " + sysarg)
              audio = await conv.get_response()
              final = ("If you get any problem Contact to Creator of this plugin @Karmaboii")
              await borg.send_message(event.chat_id, audio.text)
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @Karmaaibot `and retry!")              
