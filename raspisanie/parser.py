import requests
import json


dates_url = 'http://mmis-web.rudn-sochi.ru/api/GetRaspDates?idGroup=1467'
url = "http://mmis-web.rudn-sochi.ru/api/Rasp?idGroup=1467&sdate="

dates_html = requests.get(dates_url)
dates = json.loads(dates_html.text)
date = dates['data']['selDate']  # получаем сегодняшнюю дату

url += date

data_html = requests.get(url)
curriculum = json.loads(data_html.text)

curriculum_html_week = curriculum['data']['rasp']  # убираем лишнее из расписания
pars = ['дата', 'дисциплина', 'аудитория', 'преподаватель', 'начало', 'конец', 'деньНедели']  # данные, которые хотим достать
delete = []  # данные, которое потом удаляем, чтобы сделать словарь более компактным

for j in range(len(curriculum_html_week)):
    for i in curriculum_html_week[j]:
        if i not in pars:
            delete.append(i)  # поиск лишнего
delete = set(delete)

for j in range(len(curriculum_html_week)):
    for i in delete:
        del curriculum_html_week[j][i]  # сам процесс удаления
