import json

import requests
from aiogram.dispatcher.filters import (
    Command,
    CommandHelp,
    CommandStart,
    RegexpCommandsFilter,
)
from aiogram.types import Message
from loader import dp
from tgbot.middlewares.throttling import rate_limit


@dp.message_handler(CommandStart(), state="*")
@dp.message_handler(CommandHelp(), state="*")
@rate_limit(5, "start")
@rate_limit(5, "help")
async def send_welcome(message: Message) -> Message:
    return await message.answer(
        "Hi!\nI'm SongHelperBot!\nTo get started, send your mood with a text message."
    )


@dp.message_handler(RegexpCommandsFilter(["\/add (.+)"]), state="*")
async def add(message: Message):
    try:
        song_id = message.text.split(" ")[1]
    except IndexError:
        await message.answer("Please provide lang code")
    url = f"https://8000-mezidia-songhelper-1spk7gnsc88.ws-eu92.gitpod.io/add-song-resp/{song_id}"

    resp = requests.get(url)
    song_name = json.loads(resp.content)["song"]
    mood = json.loads(resp.content)["mood"]

    await message.answer(f"Song with {song_name} added as {mood}")
