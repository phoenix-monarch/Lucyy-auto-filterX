from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from asyncio import sleep
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
from pyrogram.types import Message, User, ChatJoinRequest


gif = [
    'https://telegra.ph/file/4e90f13338fc1a46bd9be.mp4',
    'https://telegra.ph/file/8a0de3c21f21868270a39.mp4',
    'https://telegra.ph/file/c6172c119745b0023fada.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/0d1ef0e44211c25702a95.mp4',
    'https://telegra.ph/file/dd1955c93532b567a0024.mp4',
    'https://telegra.ph/file/45fd431043e30de806b72.mp4',
    'https://telegra.ph/file/a84ac0bca1ba43bb6b005.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4'
]


@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client: Client, message: Message):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    img = random.choice(gif)
    #nothingenter
    await client.send_video(user.id,img, "**Hello {}!\nYour Request To Join {} was approved👍\n\n⚠️click /start to see my power⚠️\n\n__Powered By: @xenxd .**".format(message.from_user.mention, message.chat.title))
#by master
