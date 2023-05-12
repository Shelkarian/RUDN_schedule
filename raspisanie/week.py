from raspisanie.parser import curriculum_html_week
from raspisanie.result import result, days


def week():
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


week()
