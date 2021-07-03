# lesson 04 task 01
#
# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Три реализации функции сложения чисел от 0 до n
import timeit
import cProfile


def test_prime(func):
    lst = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def summa1(n):
    if n == 0:
        return 0
    return n + summa1(n - 1)


def summa2(n):
    spam_sum = 0
    for i in range(n+1):
        spam_sum += i
    return spam_sum


def summa3(n):
    return n * (n + 1) // 2


# test_prime(summa1)
# test_prime(summa2)
# test_prime(summa3)

# print(timeit.timeit('summa1(10)', number=100, globals=globals()))  # 0.0001571000000000003
# print(timeit.timeit('summa1(20)', number=100, globals=globals()))  # 0.00041280000000000136
# print(timeit.timeit('summa1(100)', number=100, globals=globals()))  # 0.0015536999999999981
# print(timeit.timeit('summa1(300)', number=100, globals=globals()))  # 0.005265300000000004
# print(timeit.timeit('summa1(990)', number=100, globals=globals()))  # 0.022788499999999996
#
# print(timeit.timeit('summa2(10)', number=100, globals=globals()))  # 7.719999999999949e-05
# print(timeit.timeit('summa2(20)', number=100, globals=globals()))  # 0.0001315000000000066
# print(timeit.timeit('summa2(100)', number=100, globals=globals()))  # 0.0005319999999999908
# print(timeit.timeit('summa2(300)', number=100, globals=globals()))  # 0.0015066999999999997
# print(timeit.timeit('summa2(990)', number=100, globals=globals()))  # 0.006842899999999999
#
# print(timeit.timeit('summa3(10)', number=100, globals=globals()))  # 2.0000000000006124e-05
# print(timeit.timeit('summa3(20)', number=100, globals=globals()))  # 1.7199999999994997e-05
# print(timeit.timeit('summa3(100)', number=100, globals=globals()))  # 1.8100000000007e-05
# print(timeit.timeit('summa3(300)', number=100, globals=globals()))  # 2.4700000000002498e-05
# print(timeit.timeit('summa3(990)', number=100, globals=globals()))  # 3.5800000000002496e-05

# cProfile.run('summa1(10)')  # 11/1    0.000    0.000    0.000    0.000 les4_task1.py:13(summa1)
# cProfile.run('summa1(50)')  # 51/1    0.000    0.000    0.000    0.000 les4_task1.py:13(summa1)
# cProfile.run('summa1(100)')  # 101/1    0.000    0.000    0.000    0.000 les4_task1.py:13(summa1)
# cProfile.run('summa1(300)')  # 301/1    0.000    0.000    0.000    0.000 les4_task1.py:13(summa1)
# cProfile.run('summa1(500)')  # 501/1    0.000    0.000    0.000    0.000 les4_task1.py:13(summa1)

# cProfile.run('summa2(10)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:19(summa2)
# cProfile.run('summa2(50)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:19(summa2)
# cProfile.run('summa2(100)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:19(summa2)
# cProfile.run('summa2(300)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:19(summa2)
# cProfile.run('summa2(500)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:19(summa2)

cProfile.run('summa3(10)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:26(summa3)
cProfile.run('summa3(50)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:26(summa3)
cProfile.run('summa3(100)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:26(summa3)
cProfile.run('summa3(300)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:26(summa3)
cProfile.run('summa3(500)')  # 1    0.000    0.000    0.000    0.000 les4_task1.py:26(summa3)

# Подсчет суммы чисел от 0 до n реализован в виде функций: рекурсивно, циклом и по формулам.
# Задача не очень сложная, но хорошо подходит для анализа.
#
# При помощи timeit было замерено время выполнения при n = (10, 20, 100, 300, 990)
# и составлены графики (графики можно смотреть по одному):
# http://grafikus.ru/#H8KLCADChhfCl14CA8K1wpPDi27CgzAQRcO/w4VrasONw7htfsKlw6oiVVM1agjCkcKgKijDisK/d0wwNsKqwoPClEVYw4Q3w4PDsRU5Jhc2NMKHE8KrGcKrKMOtwoZbw7rCmMOXw6F4W8OHwoUZEzPDjsKTwpnDucKlw4UCUMO6wqLCpMKnw7TDmVHDhCnCscO6w4IgfMO0NMOqaMOSwoZGDAVhw7/CtcKiPMOfPcO3w7ltw7oWwrcOwrEtbAEOAMKoLULCusOkw5ITUMKxQhUKwpdIwpQmwrAiw5XDpjBqLcKNXy7Ch8KBwpXCkcKVK1YLwqNlKlYBVRHDtT5DwoXCsMOOwqlUOz3CgcKOaGbDghRmwrYwc8O/ZjQMw4fDkcO9NMONLsOIOx5Ow7vDmWPDl8K0bR/CjgbClh/DvsKgbMKwFsOTw5N7wrUhGyXDqsOkw4RswrkGLcOzVnAbwq7CqcOUZMOnw6LDrX3DmWDCnBIuY8KfK1tsw4nClsKPw4kWPHvCpcOBwqBQw7sXw5Blw5vDiMOzM8KhwpfDi0bCtsKgG8K5w4vDvi0LWcKQLcK4wrLCiRTDisK7CBdsS8Kuw50KNhF+wp5vecOfN2HDp8Oue8OKFXtnw7UrVFjDocObw7UPDcKyZ8K3w6sEAAA=
#
# По графикам видим что рекурсивный и с циклом реализации алгоритмов имеют вычислительную сложность O(n)
# При этом, рекурсия из-за больших накладных расходов на вызов функций имеет больший константный коэффициент.
# На больших n рекурсия будет давать намного худшие результаты, чем цикл.
#
# Вычисление по формуле имеет вычислительную сложность O(1).
# То есть, при любой величине n
# (не учитывая то что при очень больших n числа будут хранится не в одном машинном слове)
# вычисление суммы будет происходить примерно за одно время.
#
# Вывод: при любых n вычисление по формуле будет быстрее, чем рекурсивно и циклом.
#
# Профилирование выявило узкое место в рекурсивных вызовах. Для остальных реализаций узких мест не выявлено.
