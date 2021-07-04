# lesson 07 task 01
#
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
#  алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#  постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100 - 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


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


def bubble_sort(arr):
    is_swap = True
    idx_swap = len(arr) - 1
    # Если на предыдущем проходе не менялись местами элементами, массив отсортирован, выходим
    while is_swap:
        is_swap = False
        # После элементов обмена массив можно не проходить. Хвост массива уже отсортирован
        for i in range(idx_swap):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                idx_swap = i
                is_swap = True


print("Исходный массив")
print(array)
bubble_sort(array)
test_sort(array, "desc")
print('Массив после сортировки')
print(array)
