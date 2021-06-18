# lesson 03 task 06
#
#  В одномерном массиве найти сумму элементов,
#  находящихся между минимальным и максимальным элементами.
#  Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 30
MIN_ITEM = -30
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if not len(array):
    print("Массив нулевой длины")
    exit(0)

min_idx = max_idx = 0
for i in range(len(array)):
    if array[i] > array[max_idx]:
        max_idx = i
    if array[i] < array[min_idx]:
        min_idx = i

summa = None
if min_idx > max_idx:
    min_range, max_range = max_idx + 1, min_idx
else:
    min_range, max_range = min_idx + 1, max_idx
for i in range(min_range, max_range):
    summa = array[i] if summa is None else (summa + array[i])

print(f'Минимальный элемент {array[min_idx]} в позиции {min_idx}')
print(f'Максимальный элемент {array[max_idx]} в позиции {max_idx}')
print("Исходный массив")
print(array)
if summa is None:
    print('Между максимальным и минимальным элементом списка нет элементов')
else:
    print(f'Сумма элементов между минимальным и максимальным: {summa}')
