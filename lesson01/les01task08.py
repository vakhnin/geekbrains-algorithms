# lesson 01 task 08
#
# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# Блок ввода
year = abs(int(input("Введите номер года: ")))

if not year % 400:
    print(f'{year} високосный')
elif not year % 100:
    print(f'{year} не високосный')
elif not year % 4:
    print(f'{year} високосный')
else:
    print(f'{year} не високосный')
