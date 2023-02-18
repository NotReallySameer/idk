from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""



SAMEER= Client(
    name="FirstProject",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("YOUR BOT STARTED SUCCESSFULLY")

SAMEER.run()
