import time


def sleep_one_sec():
    print('Перерыв 1 секунда')
    time.sleep(1)
    return 'Возвращаемое значение'
        

def sleep_two_sec():
    time.sleep(2)


# Функция для измерения быстродействия
# принимает на вход тестируемую функцию
def time_of_function(func):
    def wrapper():
        # Засекаем время перед выполнением тестируемой функции
        start_time = time.time()
        # Вызываем тестируемую функцию и 
        # cохраняем результат выполнения в переменную
        result = func()
        # Вычисляем, округляем и печатаем разницу
        # между временем старта и актуальным временем
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции: {execution_time} с.')
        # Возвращаем результат выполнения тестируемой функции
        # Если этого не сделать, результат нельзя будет использовать
        # в дальнейшем коде 
        return result
    return wrapper


# Передаём функцию sleep_one_sec() в time_of_function()
measured_sleep_one_sec = time_of_function(sleep_one_sec)
print(measured_sleep_one_sec())


# Передаём функцию sleep_two_sec() в time_of_function()
measured_sleep_two_sec = time_of_function(sleep_two_sec)
measured_sleep_two_sec()


@time_of_function
def sleep_three_time():
    time.sleep(3)
    

sleep_three_time()