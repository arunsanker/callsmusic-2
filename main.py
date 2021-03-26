from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,3855175
    API_HASH,c7d4b8b7c1259bb0b7fd836b99eb657b
    bot_token=BOT_TOKEN,1763607864:AAFKvaZBzxn5t5_VYBtI8ytZh9m6Cg4Kopo
    plugins=dict(root="handlers")
)

bot.start()
run()
