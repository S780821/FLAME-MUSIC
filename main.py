import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped, HighQualityAudio

# Import your existing objects from the Flame package
from Flame.main import call_py, bot, BOT

# ====================== MODERN PYTGCALLS SETUP ======================
# Create PyTgCalls instance (new v2+ way)
pytgcalls = PyTgCalls(bot)   # Pass your Pyrogram Client (bot) here

async def start_bot():
    print("🔥 [INFO] Starting Pyrogram Bot Client...")
    await bot.start()

    print("🎵 [INFO] Starting PyTgCalls (v2.2.x) Client...")
    await pytgcalls.start()

    print("✅ FLAME MUSIC BOT IS ONLINE!")

    # Keep the bot running
    await idle()

    # Clean shutdown (optional)
    print("🛑 Shutting down...")
    await pytgcalls.stop()
    await bot.stop()


if __name__ == "__main__":
    # This is the ONLY correct way to run async code at top level
    asyncio.run(start_bot())

    # If you have any Telethon/BOT part left (old style)
    # BOT.run_until_disconnected()   # ← you can keep this if needed, but asyncio.run is cleaner
