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
@SAMEER.on_messege(filter.command("start"))
async def start_cmd(client, message):
    print("hello i am sammy first project don't start me again")

###this is a help function lawde log
@SAMEER.on_messege(filter.command("help"))
async def help_cmd(client, message):
    print("lawda dekhne aaya hai kya biro isme its a test bot only jhatu")

print("YOUR BOT STARTED SUCCESSFULLY")

SAMEER.run()
