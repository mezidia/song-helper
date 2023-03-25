import json
import os

import requests
from aiogram.types import Message
from loader import dp
from tgbot.misc.audiodownloader import audio_downloader


@dp.message_handler()
async def echo(message: Message) -> Message:
    url = f"server.com/get-song/{message.text}"

    resp = requests.get(url)
    song_id = json.loads(resp.content)["song_id"]
    link = f"https://youtube.com/{song_id}"

    path = audio_downloader("https://www.youtube.com/watch?v={song_id}")
    audio = open(path, "rb")
    message = await message.answer_audio(audio)
    os.remove(path)
