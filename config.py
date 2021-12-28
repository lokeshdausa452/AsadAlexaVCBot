import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION = os.getenv("SESSION")
HNDLR = os.getenv("HNDLR", "/")
GROUP_MODE = os.getenv("GROUP_MODE", "True")

IMG_1 = os.getenv("IMG_1", "https://telegra.ph/file/e877179fe18a04192a00a.jpg")
IMG_2 = os.getenv("IMG_2", "https://telegra.ph/file/74d45f53fc287e9c316d1.jpg")

contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AsadAlexaVCBot"))
call_py = PyTgCalls(bot)
