# lesson 06 task 01 version 03
#
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random
import sys
from collections import deque


def show(indent, *obj):
    summa = 0
    for x in obj:
        summa += sys.getsizeof(x)
        print("  " * indent, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
        summa_spam = 0
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    summa_spam += show(indent + 1, key)
                    summa_spam += show(indent + 1, value)
                summa += summa_spam
                if len(obj) > 1:
                    print("  " * (indent + 1), f'Total: {summa_spam}')
            elif not isinstance(x, str):
                for item in x:
                    summa_spam += show(indent + 1, item)
                summa += summa_spam
                if len(obj) > 1:
                    print("  " * (indent + 1), f'Total: {summa_spam}')
    if len(obj) > 1 or indent == 0:
        print("  " * indent, f'Total: {summa}')
    return summa


SIZE = 30
MIN_ITEM = -30
MAX_ITEM = 30
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array = deque(array)

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
print(f'Минимальный элемент: {more_less} второй по минимальности элемент: {less}\n')

show(0, SIZE, MIN_ITEM, MAX_ITEM, array, 2, less, more_less)
show(0, SIZE, MIN_ITEM, MAX_ITEM, array, 2, less, more_less, "В массиве меньше двух элементов", "Исходный массив",
     f'Минимальный элемент: {more_less} второй по минимальности элемент: {less}\n')

# Windows 10 64 разрядная
# Python 3.7 32 разрядный
# Программа занимает 880 байт без учета строк в print и
# 1154 байт с учетом строк в print
