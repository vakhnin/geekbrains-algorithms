# lesson 07 task 02
#
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
import operator

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

# Функция random выдает вещественное в промежутке [0, 1)
array = [random.random() * (MAX_ITEM - MIN_ITEM) + MIN_ITEM for _ in range(SIZE)]


def test_sort(arr, compare):
    for i in range(len(arr) - 1):
        if compare == "desc":
            assert arr[i] >= arr[i + 1]
        elif compare == "asc":
            assert arr[i] <= arr[i + 1]
        else:
            assert False
    if compare == "asc":
        print('Массив отсортирован по возрастанию')
    elif compare == "desc":
        print('Массив отсортирован по убыванию')
    else:
        print('Неизвестно, как отсортирован массив')


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


print("Исходный массив")
print(array)
array = merge_sort(array)
test_sort(array, "asc")
print('Массив после сортировки')
print(array)
