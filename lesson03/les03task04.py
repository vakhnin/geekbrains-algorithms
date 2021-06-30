# lesson 03 task 04
#
# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

if not len(array):
    print("Массив нулевой длины")
    exit(0)

max_frequently_number = array[0]
for i in array:
    if array.count(i) > array.count(max_frequently_number):
        max_frequently_number = i

print(f'В массиве {array}')
print(f'Число {max_frequently_number} встречается {array.count(max_frequently_number)} раз')
