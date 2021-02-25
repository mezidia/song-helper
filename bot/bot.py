import logging
import os
import pafy

from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher(bot)

type_of_audio_file = 3
url = 'https://www.youtube.com/watch?v=kmxPFKIe4Zs'
video = pafy.new(url)
audiostreams = video.audiostreams
audiostreams[type_of_audio_file].download(filepath = './bot/')
print(audiostreams)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm SongHelperBot!\nTo get started, send your mood with a text message.")


@dp.message_handler()
async def echo(message: types.Message):
    audio = open(f'bot/{video.title}.{audiostreams[type_of_audio_file].extension}', 'rb')
    message = await bot.send_audio(message['chat']['id'], audio)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
