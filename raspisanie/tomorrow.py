from raspisanie.parser import curriculum_html_week
from raspisanie.result import result, days
import datetime


def tomorrow():
    res = ''
    tod = datetime.date.today() + datetime.timedelta(days=1)
    for i in curriculum_html_week:
        if str(tod) in i['дата']:
            t = int(datetime.datetime.today().weekday()) + 1
            if t == 8:
                t = 1
            res += days[t]
            res += '\n'
            break

    if res == '':
        return 'Выходной, зачилься)'

    for i in curriculum_html_week:
        if str(tod) in i['дата']:
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


