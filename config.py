## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

def _require_env(name: str, *, fallback: str | None = None) -> str:
    value = getenv(name, fallback)
    if value is None or not str(value).strip():
        raise RuntimeError(
            f"Missing required environment variable '{name}'. "
            "Set it in your Railway/hosting variables or .env file."
        )
    return value.strip()

def _require_any_env(*names: str) -> str:
    for name in names:
        value = getenv(name)
        if value is not None and str(value).strip():
            return value.strip()

    choices = " or ".join(f"'{name}'" for name in names)
    raise RuntimeError(
        f"Missing required environment variable {choices}. "
        "Set one of them in your Railway/hosting variables or .env file."
    )

admins = {}
SESSION_NAME = _require_any_env("SESSION_NAME", "STRING_SESSION", "SESSION_STRING")
BOT_TOKEN = _require_env("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Flamecircle_bot")
API_ID = int(getenv("API_ID", "8201417"))
API_HASH = getenv("API_HASH", "4de3ab03e330698fc1a8fbf2c85b3997")
OWNER_NAME = getenv("OWNER_NAME", "Perfect")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Xmartperson")
ALIVE_NAME = getenv("ALIVE_NAME", "Flame")
BOT_USERNAME = getenv("BOT_USERNAME", "Flamecircle_bot")
OWNER_ID = getenv("OWNER_ID", "5083524212")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Checkbt5")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Flame_project")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Flame_Updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5083524212").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/Flame-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
