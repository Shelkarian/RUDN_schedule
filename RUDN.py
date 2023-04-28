import json
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token="токен:токен")
dp = Dispatcher(bot)

url = "http://mmis-web.rudn-sochi.ru/api/Rasp?idGroup=1467&sdate=2023-04-27"
r = requests.get(url)
response_dict = json.loads(r.text)
pair = response_dict['data']['rasp']  # убираем лишнее

parsing = ['дисциплина', 'аудитория', 'преподаватель', 'начало', 'конец']  # данные, которые хотим достать

result = ['   📕Предмет: ',
          '   🏫Аудитория: ',
          '   👨‍🏫Препод: ',
          '   🕔Время: ' ]  # вывод

days = {1: '1️⃣  Понедельник',
        2: '2️⃣ Вторник',
        3: '3️⃣ Среда',
        4: '4️⃣ Четверг',
        5: '5️⃣ Пятница',
        6: '6️⃣ Суббота' }  # дни недели

days_of_the_week = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for number_day in pair:
    days_of_the_week[number_day['деньНедели']].append(number_day)


def one_pair(pairs):  # функция вывода одного дня
    vyvod = 0
    res = ''
    for data in parsing:
        if vyvod != 4:
            res += result[vyvod]
        if vyvod == 3:
            res += pairs[data] + ' - '
        else:
            res += pairs[data] + '\n'
        vyvod += 1
    return res


def week_pair(pairs):  # функция вывода недели дня
    vyvod = 0
    res = ''
    for data in parsing:
        if vyvod != 4:
            res += result[vyvod]
        if vyvod == 3:
            res += pairs[data] + ' - '
        else:
            res += pairs[data] + '\n'
        vyvod += 1
    res += '\n'
    return res


def today():
    tod = datetime.date.today()
    day_week = int(datetime.datetime.today().weekday()) + 1
    res = ''
    if day_week != 7:
        res += f'{days[day_week]}\n'
    else:
        return 'Сегодня выходной!'
    for i in pair:
        if str(tod) in i['дата']:
            pairs = i
            res += one_pair(pairs)
            res += '\n'
    return res


def tomorrow():
    tod = datetime.date.today()
    day_week = int(datetime.datetime.today().weekday()) + 2
    tod = int(tod.day) + 1
    res = ''
    if day_week != 7:
        res += f'{days[day_week]}\n'
    else:
        return 'Сегодня выходной!'
    for i in pair:
        if str(tod) in i['дата']:
            pairs = i
            res += one_pair(pairs)
            res += '\n'

    return res


def week():
    res = ''
    for one_day_of_week in days_of_the_week:
        res += f'{days[one_day_of_week]}\n'
        for j in days_of_the_week[one_day_of_week]:
            res += week_pair(j)
    return res


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
