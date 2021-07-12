# lesson 08 task 01
#
# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib

S = input('Введите строку, состоящую только из маленьких латинских букв:')
hash_substrings_set = set()

for i in range(len(S)):
    for j in range(len(S), i, -1):
        hash_str = hashlib.sha1(S[i:j].encode('utf-8')).hexdigest()
        hash_substrings_set.add(hash_str)

substrings_count = len(hash_substrings_set) - 1
# Если учитываем всю строку, как подстроку, добавляем 1 к substrings_count
# Если учитываем пустые строки, как подстроки, добавляем еще 1 к substrings_count
print(f'В строке "{S}" различных подстрок: {substrings_count}')
