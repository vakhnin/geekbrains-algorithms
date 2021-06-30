# lesson 03 task 03
#
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 30
MIN_ITEM = -30
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if not len(array):
    print("Массив нулевой длины")
    exit(0)

max_index = 0
min_index = 0

for i, n in enumerate(array):
    if n > array[max_index]:
        max_index = i
    if n < array[min_index]:
        min_index = i

print("Исходный массив")
print(array)

array[max_index], array[min_index] = array[min_index], array[max_index]
print("Массив после перестановки максимального и минимального числа в массиве")
print(array)
