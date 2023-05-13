from raspisanie.parser import curriculum_html_week, date
from raspisanie.result import result, days
import datetime

def today():
    res = ''
    for i in curriculum_html_week:
        if date in i['дата']:
            res += days[int(datetime.datetime.today().weekday()) + 1]
            res += '\n'
            break

    if res == '':
        return 'Выходной, зачилься)'

    for i in curriculum_html_week:
        if date in i['дата']:

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


