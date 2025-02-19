from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())


@dp.message_handler(text = ['Хэй!']) # text сообщения на которые стоит реагировать
async def urban_message(message):
    print("Введите команду /start, чтобы начать общение.")

@dp.message_handler(commands=['start']) #  commands после слеша стоит реагировать
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью")

@dp.message_handler() # если () оле пустое реагирует на все
async def all_message(message):
    print("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
