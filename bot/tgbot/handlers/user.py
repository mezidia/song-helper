from aiogram.dispatcher.filters import CommandStart, CommandHelp, Command
from aiogram.types import Message

from loader import dp
from tgbot.middlewares.throttling import rate_limit
import json
import requests


@dp.message_handler(CommandStart(), state="*")
@dp.message_handler(CommandHelp(), state="*")
@rate_limit(5, "start")
@rate_limit(5, "help")
async def send_welcome(message: Message) -> Message:
    return await message.answer("Hi!\nI'm SongHelperBot!\nTo get started, send your mood with a text message.")


@dp.message_handler(Command("add"), state="*")
async def add(message: Message):
    url = f'server.com/add-song-resp/{message.text}'

    resp = requests.get(url)
    song_name = json.loads(resp.content)['song']
    mood = json.loads(resp.content)['mood']

    await message.answer(f'Song with {song_name} added as {mood}')
