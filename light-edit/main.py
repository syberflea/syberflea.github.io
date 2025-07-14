def get_season(month):
    # функция должна вернуть название сезона, которому принадлежит месяц
    winter = ['январь', 'февраль', 'декабрь']
    spring = ['март', 'апрель', 'май']
    summer = ['июнь', 'июль', 'август']
    fall = ['сентябрь', 'октябрь', 'ноябрь']
    if month in winter:
        print('зима')
    elif month in spring:
        print('весна')
    elif month in summer:
        print('лето')
    elif month in fall:
        print('осень')
    else:
        print("Ошибка в написании месяца!")


# Для контроля вызовем функцию и напечатаем результат.
print(get_season('июнь'))
print(get_season('мартобрь'))