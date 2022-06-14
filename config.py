from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "9437694"))
API_HASH = getenv("API_HASH", "a92d2a0db24372f12ff42b0fe6469631")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","بوت اغاني ماس")
BOT_USERNAME = getenv("BOT_USERNAME", "G_T_Dt_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "QQWGT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SORS_mas")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b2c4ce7e2d6f302169df5.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/b2c4ce7e2d6f302169df5.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2069112486").split()))
