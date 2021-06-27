# lesson 02 task 04
#
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# Ввод числа
while True:
    try:
        n = input('Введите натуральное число: ')
        n = int(n)
        if n < 1:
            print(f'Ошибка: "{n}" должно быть больше нуля')
            continue
        break
    except ValueError:
        print(f'Ошибка: "{n}" не является натуральным числом')

# Подсчет
current_number = 1
sum_series = 0
while n > 0:
    sum_series += current_number
    current_number /= -2
    n -= 1

# Вывод результата
print(f'Сумма из {n} членов ряда = {sum_series}')
