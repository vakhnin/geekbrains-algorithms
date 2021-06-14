# lesson 02 task 09
#
# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# Ввод количества чисел и подсчитываемую цифру
while True:
    try:
        n = input('Введите количество обрабатываемых чисел: ')
        n = int(n)
        n = abs(n)
        break
    except ValueError:
        print(f'Ошибка: "{n}" не является натуральным числом')

def sum_digs(number):
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    return summa

# Подсчет
max_sum_number = 0
for _ in range(n):
    while True:
        try:
            number = input('Введите число: ')
            number = int(number)
            number = abs(number)
            break
        except ValueError:
            print(f'Ошибка: "{number}" не является натуральным числом')
    if sum_digs(number) > sum_digs(max_sum_number):
        max_sum_number = number

# Вывод результата
print(f'Число {max_sum_number} является макисмалным по сумме цифр {sum_digs(max_sum_number)}')
