import json
import requests
import datetime
from aiogram import Bot, Dispatcher, executor, types
import logging

logging.basicConfig(level=logging.INFO)


bot = Bot(token="5880976058:AAHqNEYdpO5rQeL6fA9qEkeLf2soyhXQ0Mg")
dp = Dispatcher(bot)


url = "http://mmis-web.rudn-sochi.ru/api/Rasp?idGroup=1467&sdate=2023-04-27"
r = requests.get(url)
response_dict = json.loads(r.text)
pair = response_dict['data']['rasp']

li = ['дисциплина', 'аудитория', 'преподаватель', 'начало', 'конец']
result = ['Предмет: ', ' Аудитория: ', ' Препод: ', ' Время: ']
dayz = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота'}
days = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for i in pair:
    days[i['деньНедели']].append(i)


def one_pair(pairs):
    vyvod = 0
    res = ''
    for k in li:
        if vyvod != 4:
            res += result[vyvod]
        if vyvod == 3:
            res += pairs[k] + ' - '
        else:
            res += pairs[k] + '\n'
        vyvod += 1
    return res

def week_pair(pairs):
    vyvod = 0
    res = ''
    for k in li:
        if vyvod != 4:
            res += result[vyvod]
        if vyvod == 3:
            res += pairs[k] + ' - '
        else:
            res += pairs[k] + '\n'
        vyvod += 1
    res += '\n'
    return res


def today():
    tod = datetime.date.today()
    res = ''
    for i in pair:
        if str(tod) in i['дата']:
            pairs = i
            res += one_pair(pairs)
            res += '\n'
    return res

def next_day():
    tod = datetime.date.today()
    tod = int(tod.day) + 1
    res = ''

    for i in pair:
        if str(tod) in i['дата']:
            pairs = i
            res += one_pair(pairs)
            res += '\n'
    return res

def week():
    res = ''
    for i in days:
        res += f'День: {dayz[i]}\n'
        res += '---------------\n'
        for j in days[i]:
            res += week_pair(j)
    return res

@dp.message_handler(commands=['today'], chat_type=types.ChatType.GROUP)
async def get_today(message: types.Message):
    today_pairs = today()
    await message.answer(today_pairs)

@dp.message_handler(commands=['next_day'], chat_type=types.ChatType.GROUP)
async def get_next_day(message: types.Message):
    tomorrow_pairs = next_day()
    await message.answer(tomorrow_pairs)

@dp.message_handler(commands=['week'], chat_type=types.ChatType.GROUP)
async def get_week(message: types.Message):
    week_pairs = week()
    await message.answer(week_pairs)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

