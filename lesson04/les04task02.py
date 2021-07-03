# lesson 04 task 02
#
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию:
# Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# Простое n число
import timeit
import cProfile
from math import sqrt


def test_prime(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, item in enumerate(lst, start=1):
        assert item == func(i)
        print(f'Test {i} OK')


def sieve(n):
    sieve_arr = [i for i in range(n * n + 2)]
    sieve_arr[1] = 0
    len_sieve_arr = len(sieve_arr)
    for i in range(2, len_sieve_arr):
        if sieve_arr[i] != 0:
            j = i + i
            while j < len_sieve_arr:
                sieve_arr[j] = 0
                j += i

    for i in sieve_arr:
        if i != 0:
            if n > 1:
                n -= 1
            else:
                return i


def prime(n):
    shift = 2
    if n == 1:
        return 2
    prime_arr = [3, 5, 7]
    for i in range(11, n * n + 2, 2):
        if len(prime_arr) >= n + shift:
            break
        sqrt_i = sqrt(i)
        for j in prime_arr:
            if j > sqrt_i:
                prime_arr.append(i)
                break
            if i % j == 0:
                break
    return prime_arr[n - shift]


# test_prime(sieve)

# print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.0024107000000000017
# print(timeit.timeit('sieve(50)', number=100, globals=globals()))  # 0.0841172
# print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.3424142
# print(timeit.timeit('sieve(300)', number=100, globals=globals()))  # 3.5862416999999995
# print(timeit.timeit('sieve(500)', number=100, globals=globals()))  # 11.060683000000001

# cProfile.run('sieve(10)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:15(<listcomp>)
# cProfile.run('sieve(50)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:15(<listcomp>)
# cProfile.run('sieve(100)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:15(<listcomp>)
# cProfile.run('sieve(300)')  # 1    0.003    0.003    0.003    0.003 les4_task2.py:15(<listcomp>)
# cProfile.run('sieve(500)')  # 1    0.009    0.009    0.009    0.009 les4_task2.py:15(<listcomp>)

# test_prime(prime)

# print(timeit.timeit('prime(10)', number=100, globals=globals()))  # 0.000981199999999998
# print(timeit.timeit('prime(50)', number=100, globals=globals()))  # 0.007228699999999998
# print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 0.022486599999999995
# print(timeit.timeit('prime(300)', number=100, globals=globals()))  # 0.09231220000000001
# print(timeit.timeit('prime(500)', number=100, globals=globals()))  # 0.16714230000000002

cProfile.run('prime(10)')  # 16    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
cProfile.run('prime(50)')  # 116    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
cProfile.run('prime(100)')  # 277    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
cProfile.run('prime(300)')  # 995    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
cProfile.run('prime(500)')  # 1792    0.000    0.000    0.000    0.000 {built-in method math.sqrt}

# Нахождение n простого числа реализовано двумя функциями: решето Эратосфена и проверка делимости на меньшие делители.
#
# При помощи timeit было замерено время выполнения при n = (10, 50, 100, 300, 500)
# и составлены графики (графики можно смотреть по одному):
# http://grafikus.ru/#H8KLCADDswXCl14CA8K1UMORasKEMBDDvMKXPMKHwrDCm2TCk8Oowq/ClD7DtMKowqXDksOzwpQqwq1yw5zCv8OfRsKjacKpFsO6w5DChWTDh8KZw5k1w4xVwoxNfRHCpRDCksORw5PCuMKgw6fDlMOHw7PDksKnw40zZcOPwpTCmMOkw7nDpMOmARjCvTLCohnCvcO0DHFGwqLCvAoTwq/CgcKpbmDCqsKNK8KRAX8xD8OxGld/XA4KQFsEL27CksKNScKmL3LCsMKIXkdZw6fDqcKsG8OLw6N2w5bDjcKqwptNN8KKwoJjwoMrUlE0w5rDvMKfw5XCiMKow4DCgQs8wroURiPCrcOGw6TCisKcw5vDocO8Dhd+cEzDhhzDu8K6w7rCqMKYPMOXwpcqwqXDkzdtO8OESGF7w57DnyLChMOCBcKCXMOuME4oAMOsccKcwqDDiQfDgsK8wokOwpIFwoVYBD7DsC3CscKdaEFpSzbCmMO8PsO9b8OZdsOvdcOzS8K2w6zDqsO6wrcZS3ESw6UDSMKUw7h4wrsDworCkW1IIgMAAA==
#
# Оба алгоритма имеют вычислительную сложность больше O(n) и меньше O(n^2).
# По теории алгоритмы имеют вычислительную сложность O(n log log n).
# При этом алгоритм проверки делимости имеет меньший коэффициент. При n == 500 алгоритм работает в 66 раз быстрее.
# При увеличении n разрыв будет увеличиваться.
#
# Решето Эратосфена требует с1*n^2 дополнительной памяти, алгоритм проверки делимости только c2*n
#
# Вывод: При любых n лучше использовать алгоритм проверки делимости.
#
# Профилирование выявило узкое место в решете Эратосфена: создание начального массива (строка 15)
# В алгоритме проверки делимости профилированием выявлено узкое место:
# вычисление корня из текущего проверяемого числа (строка 41)
