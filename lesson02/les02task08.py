# lesson 02 task 08
#
# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.

# Ввод количества чисел и подсчитываемую цифру
while True:
    try:
        n = input('Введите количество обрабатываемых чисел: ')
        n = int(n)
        n = abs(n)
        break
    except ValueError:
        print(f'Ошибка: "{n}" не является натуральным числом')
while True:
    try:
        dig = input('Введите подсчитываемую цифру: ')
        dig = int(dig)
        dig = abs(dig)
        break
    except ValueError:
        print(f'Ошибка: "{dig}" не является цифрой')

# Подсчет
sum_dig = 0
for _ in range(n):
    while True:
        try:
            number = input('Введите число: ')
            number = int(number)
            number = abs(number)
            break
        except ValueError:
            print(f'Ошибка: "{number}" не является цифрой')
    while number > 0:
        if number % 10 == dig:
            sum_dig += 1
        number //= 10

# Вывод результата
print(f'Цифра {dig} встречалась {sum_dig} раз')
