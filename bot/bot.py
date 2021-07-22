import logging
import os
import asyncio
import aiohttp
import requests
import json
from audiodownloader import audio_downloader

from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv
# from songhelper import *

load_dotenv()

logging.basicConfig(level=logging.INFO)

Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm SongHelperBot!\nTo get started, send your mood with a text message.")


@dp.message_handler()
async def echo(message: types.Message):
    url = f'server.com/get-song/{message.text}'

    resp = requests.get(url)
    song_id = json.loads(resp.content)['song_id']
    link = f'https://youtube.com/{song_id}'

    path = audio_downloader('https://www.youtube.com/watch?v={song_id}')
    audio = open(path, 'rb')
    message = await bot.send_audio(message['chat']['id'], audio)
    os.remove(path)


@dp.message_handler()
async def add(message: types.Message):
    url = f'server.com/add-song-resp/{message.text}'

    resp = requests.get(url)
    song_name = json.loads(resp.content)['song']
    mood = json.loads(resp.content)['mood']

    await message.answer(f'Song with {song_name} added as {mood}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
