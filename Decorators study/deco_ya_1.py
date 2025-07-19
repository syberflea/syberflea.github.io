global_variable = 'Глобальная'


def some_func1(passed_variable):
    local_variable = 'Локальная'
    return(f'{global_variable} '
           f'{local_variable} '
           f'{passed_variable}')

           
def some_func(passed_variable):
    local_variable = 'Локальная'

    def inside_func():
        inside_local_variable = 'Внутренняя'
        return(f'{global_variable} '
               f'{local_variable} '
               f'{passed_variable} '
               f'{inside_local_variable}')
    return inside_func


#some_func('Параметр')
#print(some_func('Параметр'))
# Здесь вызывается функция some_func() 
# и результат её работы присваивается переменной kind_of_magic 
kind_of_magic = some_func('Параметр')

# Здесь рождается магия: some_func() вернула функцию, 
# значит, kind_of_magic — это функция
# и её можно вызвать:
print(kind_of_magic())
# Будет напечатано: Глобальная Локальная Параметр Внутренняя

# Можно создать ещё одну функцию
another_magic = some_func('Другой параметр')
print(another_magic())
