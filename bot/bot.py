import logging
import os
import asyncio
import aiohttp
# import requests
from audiodownloader import audio_downloader

from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv
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
    # msg_to_server = {'msg': message.text}
    # song = make_request(msg_to_server).text
    path = audio_downloader('https://www.youtube.com/watch?v=jdGe4w4LADM')
    audio = open(path, 'rb')
    message = await bot.send_audio(message['chat']['id'], audio)
    os.remove(path)


@dp.message_handler()
async def add(message: types.Message):
    # msg_to_server = {'msg': 'add_new/' + message.text}
    # song = make_request(msg_to_server).text
    path = audio_downloader('https://www.youtube.com/watch?v=jdGe4w4LADM')
    audio = open(path, 'rb')
    message = await bot.send_audio(message['chat']['id'], audio)
    os.remove(path)


async def make_request(mood_text: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://api.github.com/users/{mood_text}') as response:
            return await response.json()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
