# lesson 02 task 05
#
# Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме:
# по десять пар "код-символ" в каждой строке.

START_CHAR_CODE = 32
END_CHAR_CODE = 127

for char_code in range(START_CHAR_CODE, END_CHAR_CODE + 1):
    if char_code != START_CHAR_CODE \
            and not (char_code - START_CHAR_CODE) % 10:
        print()
    print(f'{char_code:3d}-{chr(char_code)} ', end="")
