def some_func(passed_variable):
    def inside_func(passed_inside_variable):
        return f'{passed_variable}, {passed_inside_variable}'
    return inside_func

# Создали функцию hello()
hello = some_func('Привет')
# В контексте функции hello() значением passed_variable будет строка 'Привет'

# Вызываем hello() с параметром для inside_func()
print(hello('Стёпа'))
# Будет напечатано: Привет, Стёпа

byebye = some_func('До свидания')
# В контексте функции byebye() 
# значением passed_variable будет строка 'До свидания'

print(byebye('Марк Лутц'))
# Будет напечатано: До свидания, Марк Лутц

# Но значение переменной passed_variable в контексте hello() cохранилось:
# оно по-прежнему 'Привет'
print(hello('Лера'))