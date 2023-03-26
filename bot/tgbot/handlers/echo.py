import json
import os

import requests
from aiogram.types import Message
from loader import dp
from tgbot.misc.audiodownloader import convert_to_mp3, download


@dp.message_handler()
async def echo(message: Message) -> Message:
    url = f"https://8000-mezidia-songhelper-1spk7gnsc88.ws-eu92.gitpod.io/get-song/{message.text}"

    resp = requests.get(url)
    song_id = json.loads(resp.content)["song_id"]

    video_path = download(f"https://www.youtube.com/watch?v={song_id}")
    audio_path = f"{video_path.rsplit('.', maxsplit=1)[0]}.mp3"
    convert_to_mp3(video_path, audio_path)
    audio = open(audio_path, "rb")
    message = await message.answer_audio(audio)
    os.remove(video_path)
    os.remove(audio_path)
