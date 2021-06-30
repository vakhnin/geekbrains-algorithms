# lesson 03 task 09
#
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE1 = 5
SIZE2 = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE2)] for _ in range(SIZE1)]

if not len(matrix) or not len(matrix[0]):
    print("По одному или двум измерениям матрица имеет нулевую длину")
    exit(0)

max_min_colomn = None
for j in range(SIZE2):
    min_colomn = matrix[0][j]
    for i in range(SIZE1):
        if matrix[i][j] < min_colomn:
            min_colomn = matrix[i][j]
    if max_min_colomn is None or min_colomn > max_min_colomn:
        max_min_colomn = min_colomn

print("Исходная матрица")
print(*matrix, sep='\n')
print(f'максимальный элемент среди минимальных элементов столбцов матрицы: {max_min_colomn}')
