import json
import os

import requests
from aiogram.types import Message
from loader import dp
from tgbot.misc.audiodownloader import convert_to_mp3, download


@dp.message_handler()
async def echo(message: Message) -> Message:
    # url = f"server.com/get-song/{message.text}"

    # resp = requests.get(url)
    # song_id = json.loads(resp.content)["song_id"]
    song_id = "EOA1wBw_Jt4"

    video_path = download(f"https://www.youtube.com/watch?v={song_id}")
    audio_path = f"{video_path.rsplit('.', maxsplit=1)[0]}.mp3"
    convert_to_mp3(video_path, audio_path)
    audio = open(audio_path, "rb")
    message = await message.answer_audio(audio)
    os.remove(video_path)
    os.remove(audio_path)
