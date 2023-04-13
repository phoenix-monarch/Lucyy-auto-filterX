"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters

from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "<b>I m Lucyy.... I'm Working Properly</b>" 
# -- Constants End -- #


@Client.on_message(filters.command("alive", "/") & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", "/") & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"<b>Pong!\n{time_taken_s:.3f} ms\n\n©ᴛꜱᴜɴᴀᴅᴇ™</b>")






