import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

Token = os.getenv('TOKEN')
bot = Bot(token = Token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)