#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= API_ID, 15496141
    api_hash="API_HASH", 22f918ca3684f4ceb5d465a48be1b1c1
    bot_token="BOT_TOKEN", 5449428483:AAHU21zWFqfE_k-YfcMOU_5m1oQCFfshCKw
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
