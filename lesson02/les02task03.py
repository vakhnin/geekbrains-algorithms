# lesson 02 task 03
#
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# Ввод числа
while True:
    try:
        n = input('Введите натуральное число: ')
        n_copy = int(n)
        n = abs(n_copy)
        break
    except ValueError:
        print(f'Ошибка: "{n}" не является натуральным числом')

# Подсчет
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

# Вывод результата
zero_fill = "0" * (len(str(abs(n_copy))) - len(str(rev)))
print(f'{"-" if n_copy < 0 else ""}{zero_fill}{rev} '
      f'является обратным к {n_copy}')
