from raspisanie.result import result, days
import requests
import json


dates_url = 'http://mmis-web.rudn-sochi.ru/api/GetRaspDates?idGroup=1467'
url = "http://mmis-web.rudn-sochi.ru/api/Rasp?idGroup=1467&sdate="

dates_html = requests.get(dates_url)
dates = json.loads(dates_html.text)
date = dates['data']['selDate']  # получаем сегодняшнюю дату
n_date = int(date[-2:]) + 7
date = date[:-2] + str(n_date)
url += date

data_html = requests.get(url)
curriculum = json.loads(data_html.text)

curriculum_html_week = curriculum['data']['rasp']  # убираем лишнее из расписания

def next_week():
    res = ''

    for i in curriculum_html_week:

        day_week = i['деньНедели']

        if days[day_week] not in res:
            res += days[day_week]
            res += '\n'

        res += result[0]
        res += i['дисциплина']
        res += '\n'

        res += result[1]
        res += i['аудитория']
        res += '\n'

        res += result[2]
        res += i['преподаватель']
        res += '\n'

        res += result[3]
        res += i['начало']
        res += ' - '
        res += i['конец']
        res += '\n'
        res += '\n'
    return res


next_week()
