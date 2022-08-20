## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAZrFmew2qg6fXlzeqZiuI5qBzZSNwkSkvdouU16e5y8ZCWU1RUtejuo5c5L9Hru7v3o0-m_6rV2muYbdr7ApMpaR6__Knq1cU3KPjLAN8uiRWA1RlZk-j7JRB44VGOZ0OEuhsrObao2qh14foHNndLvJdhBfrYi7jppVPLidXI8B5XDw9AX9HV_S05GAb16TERMsrTk5fiNelRSozXJIG2X1XUdpXm0I7gawLvaf6wRpqodo8Z0zEEBh-7UD_RFyOMcuGA92K0uWCuDkCOwwz19p1j7ESMtox2AAYU8sUefZ8OnGbpWOPXIj9DwqN2XBhAOP-WILTjfJMpXYCIstIfAAAAAU38sR4A")
BOT_TOKEN = getenv("BOT_TOKEN", "5423656818:AAEIPfLPVougR6pO4bzzVbsMu_WnDxZzK5E")
BOT_NAME = getenv("BOT_NAME", "ENA")
API_ID = int(getenv("API_ID", "9447710"))
API_HASH = getenv("API_HASH", "bfbdd55dfcc54fe2832d1ff4bbe234e2")
OWNER_NAME = getenv("OWNER_NAME", "faust")
OWNER_USERNAME = getenv("OWNER_USERNAME", "U_G_II")
ALIVE_NAME = getenv("ALIVE_NAME", "FAUST")
BOT_USERNAME = getenv("BOT_USERNAME", "E_V_Abot")
OWNER_ID = getenv("OWNER_ID", "782126582")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "EV_C6")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "U_G_2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Goto90")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "782126582").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
