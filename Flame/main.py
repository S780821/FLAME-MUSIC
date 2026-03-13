import os
import sys
import random
import asyncio
from telethon.errors import FloodWaitError
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

if not hasattr(filters, "edited"):
    filters.edited = filters.create(
        lambda _, __, message: bool(getattr(message, "edit_date", None))
    )


bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Flame.Player"},
)

BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
except FloodWaitError as e:
    print(f"⏳ FloodWaitError: Sleeping {e.seconds} seconds...")
    asyncio.run(asyncio.sleep(e.seconds + 5))  # extra 5s safety
    BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

Test = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'Flame.Player'})
call_py = PyTgCalls(Test)
