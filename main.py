import asyncio
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from pyrogram import Client, idle
from pytgcalls import PyTgCalls

# Import your existing Flame objects (keep these unchanged)
from Flame.main import call_py, bot, BOT

# ====================== PYTGCALLS SETUP ======================
pytgcalls = PyTgCalls(bot)  # Pass your Pyrogram client

class _HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, format, *args):  # noqa: A003
        return


def start_healthcheck_server():
    """Start a tiny HTTP server when PORT is set (Railway web service mode)."""
    port = os.getenv("PORT")
    if not port:
        return

    server = HTTPServer(("0.0.0.0", int(port)), _HealthHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"🌐 Healthcheck server listening on 0.0.0.0:{port}")

async def start_bot():
    start_healthcheck_server()
    
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
