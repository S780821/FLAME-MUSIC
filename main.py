import asyncio
from pytgcalls import idle
from Flame.main import call_py, bot, BOT

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    bot.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    call_py.start()
    idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
BOT.run_until_disconnected()
