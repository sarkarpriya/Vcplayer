import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("BQFHJTwAtTLa-S1K9AOf0O87npPlBklgidnF-rODKxtg31BzqdeEkgfMFiPXC6e3XWmIXRvg-1ISyUNCwXJ570hgySqJLLVkwKVvTqSw-AiI9Z5g2FjxvL1NJTpirCKnw_pxizJ6WryfkeGTBqWoGBBS3NP-9lfd-onZvuLWFSRnhavWsRbX_NCDyXlHyv4_V_ydJ_lGMy_TvWTzXlaKw9BNi0OSfgBbuNeFeamope9VXAd4Hfpt8aW5BfIDbVbheLFk3nmFuKotbQUxH0IOx5Cw9Aftg-s-VjvSF4jLaLv2MuHaWAkFBLAhVFVeqFzs5w0bxdx3Uaji8ClPdXqNpQWbY8h6NQAAAAHGZNYDAA", "session")
BOT_TOKEN = getenv("8528477073:AAHKXOwvHDXN9TMbNKtnWrg-OWJJd69dQOM")
BOT_NAME = getenv("SARKAR MUSIC")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@Wormgpt57_bot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("21439804"))
API_HASH = getenv("c0366a3f6c4ad144df1e430b1c22c9da")
BOT_USERNAME = getenv("@Vehtonum1_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Dead0XD")
OWNER_NAME = getenv("OWNER_NAME", "SARKAR GOLU")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AwesomeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5478136161").split()))
