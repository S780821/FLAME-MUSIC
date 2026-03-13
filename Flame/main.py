import os
import sys
import random
import asyncio
import time
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

# ================== BOT CLIENT WITH FLOOD PROTECTION ==================
BOT = None
try:
    BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    print("✅ Bot logged in successfully!")
except FloodWaitError as e:
    print(f"⏳ FloodWaitError: Waiting {e.seconds} seconds...")
    # Avoid asyncio.run() here, since closing a temporary loop at import time
    # can interfere with Telethon's own loop resolution in the main thread.
    time.sleep(e.seconds + 10)  # extra 10s safety
    BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    print("✅ Bot logged in after flood wait!")
except Exception as e:
    print(f"❌ Unexpected error starting BOT: {e}")
    raise
# =====================================================================


user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

Test = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'Flame.Player'})
call_py = PyTgCalls(Test)
