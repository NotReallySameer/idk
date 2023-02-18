from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


### client set-up system lawde
SAMEER= Client(
    name="FirstProject",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

###thia is a start function
@SAMEER.on_messege(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("hello i am sammy first project don't start me again")

###this is a help function lawde log
@SAMEER.on_messege(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text("lawda dekhne aaya hai kya biro isme its a test bot only jhatu")

print("YOUR BOT STARTED SUCCESSFULLY")

SAMEER.run()
