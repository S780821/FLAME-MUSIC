## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCKDUuOb_DmfEaIYsXAMhDxQrqc6O_sRKV8oeFd9bLQws-oEBIdHH2CFroP8-e0TkerOaW97Q7IK7CicGPPvYSWrVQWvFn6ls7jR6xvaDTq-LO-0FO4IHqky9JkRQV3btjQAHpxubd2LOUZwSfWwHQn1Hw_smMkiNaUoOVKeNRjDNSJLqRD_CSQkJ2D9ffceN79TIidsiF5cV2Isa3KsAiVR6p4exklPTvi3yvXuZ0XkvZttqnBqiH_2QZVWN978GDEhjFpFAlBogmnJybl1ieWlvt1MoHDbZrkOnU5hlytfL0MFyEcaoovEbdKNl8hm8HsDI-FW5IMkq8eh1k4E9WWAAAAAUMWqxMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5567859075:AAHMuH-GJoaUY8J9oG-4T9yOagb7gGplA2M")
BOT_NAME = getenv("BOT_NAME", "mahakal")
API_ID = int(getenv("API_ID", "18871550"))
API_HASH = getenv("API_HASH", "d65d43db858a8c1088dabec0dfbd0491")
OWNER_NAME = getenv("OWNER_NAME", "Mahakal")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@ITS_RED_TEAM_DEVEL_OP")
ALIVE_NAME = getenv("ALIVE_NAME", "Mahakal")
BOT_USERNAME = getenv("BOT_USERNAME", "@sad_music_op_bot")
OWNER_ID = getenv("OWNER_ID", "5350202392")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Mahakal")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "The_Friends_Forever")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "The_Friends_Forever")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5350202392").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/0a0a17bc654860f5d12b2.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/0a0a17bc654860f5d12b2.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/Flame-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
