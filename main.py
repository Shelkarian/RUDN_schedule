from aiogram import Bot, Dispatcher, executor, types
import logging

from raspisanie.today import today
from raspisanie.tomorrow import tomorrow
from raspisanie.week import week
from raspisanie.next_week import next_week

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5880976058:AAHqNEYdpO5rQeL6fA9qEkeLf2soyhXQ0Mg")
dp = Dispatcher(bot)


@dp.message_handler(commands=['today'])
async def get_today(message: types.Message):
    today_pairs = today()
    await message.answer(today_pairs)


@dp.message_handler(commands=['tomorrow'])
async def get_next_day(message: types.Message):
    tomorrow_pairs = tomorrow()
    await message.answer(tomorrow_pairs)


@dp.message_handler(commands=['week'])
async def get_week(message: types.Message):
    week_pairs = week()
    await message.answer(week_pairs)
@dp.message_handler(commands=['next_week'])
async def get_week(message: types.Message):
    next_week_pairs = next_week()
    await message.answer(next_week_pairs)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
