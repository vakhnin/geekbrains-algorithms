# lesson 07 task 03
#
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой — не больше медианы.

import random
from statistics import median

m = 5
SIZE = 2 * m + 1
MIN_ITEM = -30
MAX_ITEM = 30

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def test_median(func):
    for i in range(20):
        arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
        assert median(arr) == func(arr)
    print('Тесты пройдены')


def quickselect_median(arr):
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) / 2)
    else:
        return 0.5 * (quickselect(arr, len(arr) / 2 - 1) +
                      quickselect(arr, len(arr) / 2))


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


print("Исходный массив")
print(array)
test_median(quickselect_median)
print(f'Медиана: {quickselect_median(array)}')
print('Отсортированный массив (для быстрой проверки)')
print(sorted(array))
