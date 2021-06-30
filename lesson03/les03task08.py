# lesson 03 task 08
#
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print('Заполните матрицу данными')
matrix = list()
for i in range(4):
    row = list()
    sum_row = 0
    for j in range(4):
        while True:
            x = input(f'Введите элемент матрицы [{j}:{i}]: ')
            try:
                x = float(x)
                break
            except ValueError:
                print(f'Ошибка: "{x}" не является числом')
        sum_row += x
        row.append(x)
    row.append(sum_row)
    matrix.append(row)

print('Итоговая матрица:')
max_len = 0
for i in range(4):
    for j in range(5):
        if len(str(matrix[i][j])) > max_len:
            max_len = len(str(matrix[i][j]))
for i in range(4):
    for j in range(5):
        spaces = " " * (max_len - len(str(matrix[i][j])))
        print(f'{spaces}{matrix[i][j]}', end=" ")
    print()
