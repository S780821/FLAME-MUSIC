import asyncio
from pyrogram import Client, idle
from pytgcalls import PyTgCalls

# Correct imports for py-tgcalls 2.2.11 (this fixes the error)
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.audio_parameters import HighQualityAudio

# Import your existing Flame objects (keep these unchanged)
from Flame.main import call_py, bot, BOT

# ====================== PYTGCALLS SETUP ======================
pytgcalls = PyTgCalls(bot)  # Pass your Pyrogram client

async def start_bot():
    print("🔥 Starting Pyrogram Bot...")
    await bot.start()

    print("🎵 Starting PyTgCalls v2.2.11...")
    await pytgcalls.start()

    print("✅ FLAME MUSIC BOT IS NOW ONLINE & READY!")

    # Keep the bot running forever
    await idle()

    # Clean shutdown
    await pytgcalls.stop()
    await bot.stop()


if __name__ == "__main__":
    asyncio.run(start_bot())
