# Допишите нужные импорты.
from datetime import datetime, timedelta

second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour

def timedelta_days(datetime_str_1, datetime_str_2):
    # Напишите тело функции.
    time_format = '%Y/%m/%d %H:%M:%S'
    datetime_1 = datetime.strptime(datetime_str_1, time_format)
    datetime_2 = datetime.strptime(datetime_str_2, time_format)
    return timedelta.total_seconds(datetime_2 - datetime_1) // day


difference = timedelta_days('2019/05/10 00:00:00', '2019/10/04 00:00:00')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')
