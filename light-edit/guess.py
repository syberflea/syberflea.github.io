import random


def guess_number():
    # Загадываем число от 1 до 100
    secret_number = random.randint(1, 100)

    print("Привет! Загадай число от 1 до 100.")
    print("Я попробую его угадать за 7 попыток или меньше.")

    # Устанавливаем счетчик попыток
    attempts = 7

    while attempts > 0:
        # Запрашиваем предполагаемое число от пользователя
        guess = int(input("Введите предполагаемое число: "))

        if guess < secret_number:
            print("Загаданное число больше.")
        elif guess > secret_number:
            print("Загаданное число меньше.")
        else:
            print("Поздравляю! Вы угадали число!")
            return

        attempts -= 1
        print(f"Осталось попыток: {attempts}")

    print(f"Увы, вы исчерпали все попытки. Загаданное число было: {secret_number}")


guess_number()
