# lesson 02 task 06
#
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше
# введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано,
# то вывести загаданное число.
import random

number_to_guess = random.randint(0, 100)
for i in range(9, -1, -1):
    # Ввод числа с проверкой
    while True:
        try:
            user_guess = input('Угадайте число от 0 до 100: ')
            user_guess = int(user_guess)
            if user_guess < 0:
                print(f'Ошибка: "{user_guess}" должно быть больше или равно нулю')
                continue
            elif user_guess > 100:
                print(f'Ошибка: "{user_guess}" должно быть меньше или равно ста')
                continue
            break
        except ValueError:
            print(f'Ошибка: "{user_guess}" не является натуральным числом')

    # Проверяем угадано ли число и последняя ли это попытка
    if number_to_guess == user_guess:
        print(f'Вы угадали загаданное число за {10 - i} попыток!')
        print(f'Загаданное число: {number_to_guess}')
        break
    if not i:
        print('Вы не угадали загаданное число за 10 попыток!')
        print(f'Загаданное число: {number_to_guess}')
        break

    # Выводим больше или меньше загаданное число и сколько осталось попыток
    if number_to_guess < user_guess:
        print(f'Загаданное число меньше, чем {user_guess}')
    elif number_to_guess > user_guess:
        print(f'Загаданное число больше, чем {user_guess}')
    print(f'У Вас осталось {i} попыток')
