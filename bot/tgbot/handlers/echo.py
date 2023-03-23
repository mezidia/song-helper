from aiogram.types import Message

from loader import dp
from tgbot.misc.audiodownloader import audio_downloader

import os
import requests


@dp.message_handler()
async def echo(message: Message) -> Message:
    url = f'server.com/get-song/{message.text}'

    resp = requests.get(url)
    song_id = json.loads(resp.content)['song_id']
    link = f'https://youtube.com/{song_id}'

    path = audio_downloader('https://www.youtube.com/watch?v={song_id}')
    audio = open(path, 'rb')
    message = await bot.send_audio(message['chat']['id'], audio)
    os.remove(path)

