import asyncio
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import AudioPiped, HighQualityAudio
from Flame.main import call_py, bot, BOT

app = PyTgCalls(client)   # client = your Pyrogram Client instance
await app.start()

# Example: play audio file or yt stream
await app.play(
    chat_id,
    AudioPiped(
        path_or_url,                   # e.g. "song.mp3" or "https://..."
        audio_parameters=HighQualityAudio()
    )
)

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
BOT.run_until_disconnected()
