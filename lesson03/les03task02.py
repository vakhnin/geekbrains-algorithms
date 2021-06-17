# lesson 03 task 02
#
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями
# 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 30
MIN_ITEM = -30
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if not len(array):
    print("Массив нулевой длины")
    exit(0)

even_index_arr = []

for i in range(len(array)):
    if not array[i] % 2:
        even_index_arr.append(i)

print("Исходный массив")
print(array)
print("Массив индексов четных чисел")
print(even_index_arr)
