# lesson 03 task 07
#
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 30
MIN_ITEM = -30
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if len(array) < 2:
    print("В массиве меньше двух элементов")
    exit(0)

if array[1] > array[0]:
    less, more_less = array[1], array[0]
else:
    less, more_less = array[0], array[1]

for i in range(2, len(array)):
    if array[i] < more_less:
        less, more_less = more_less, array[i]
    elif array[i] < less:
        less = array[i]

print("Исходный массив")
print(array)
print(f'Минимальный элемент: {more_less} второй по минимальности элемент: {less}')
