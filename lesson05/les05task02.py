# lesson 05 task 02
#
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив,
# элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
#
# В этом задании использована коллекция deque

from collections import deque
import random

TABLE = tuple("0123456789ABCDEF")


def sum_hex(a_, b_):
    c = deque()
    transfer = 0

    if len(a_) < len(b_):
        a_, b_ = b_, a_

    while a_:
        c1 = TABLE.index(a_.pop())
        c2 = TABLE.index(b_.pop()) if b_ else 0
        res_spam = c1 + c2 + transfer
        if res_spam >= len(TABLE):
            res_spam -= len(TABLE)
            transfer = 1
        else:
            transfer = 0
        c.appendleft(TABLE[res_spam])
    if transfer:
        c.appendleft(TABLE[transfer])
    return c


def mult_hex(a_, b_):
    result = deque('0')
    shift = deque()

    while b_:
        a_copy = a_.copy()
        c2 = TABLE.index(b_.pop())
        c = deque()
        transfer = 0
        while a_copy:
            c1 = TABLE.index(a_copy.pop())
            res_spam = c1 * c2 + transfer
            if res_spam >= len(TABLE):
                transfer = res_spam // len(TABLE)
                res_spam %= len(TABLE)
            else:
                transfer = 0
            c.appendleft(TABLE[res_spam])
        if transfer:
            c.appendleft(TABLE[transfer])
        result = sum_hex(result, (c + shift))
        shift.append('0')
    return result


def test_sum(func):
    for i in range(15):
        a_ = random.randint(0, 5000)
        b_ = random.randint(0, 5000)
        assert f'{a_+b_:X}' == ''.join(func(deque(f'{a_:X}'), deque(f'{b_:X}')))
        print(f'Test {a_:X}+{b_:X}={a_+b_:X} OK')


def test_mult(func):
    for i in range(15):
        a_ = random.randint(0, 5000)
        b_ = random.randint(0, 5000)
        assert f'{a_*b_:X}' == ''.join(func(deque(f'{a_:X}'), deque(f'{b_:X}')))
        print(f'Test {a_:X}*{b_:X}={a_+b_:X} OK')


test_sum(sum_hex)
test_mult(mult_hex)

a = input('Введите первое число:')
a = a.upper()
b = input('Введите второе число:')
b = b.upper()

print(f'{"".join(a)} + {"".join(b)} = {"".join(sum_hex(deque(a), deque(b)))}')
print(f'{"".join(a)} * {"".join(b)} = {"".join(mult_hex(deque(a), deque(b)))}')
