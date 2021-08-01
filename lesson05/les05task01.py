# lesson 05 task 01
#
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
#
# В этом задании использована коллекция dictionary

QUARTERS = 4
companies = {}

n = int(input('Введите количество преприятий:'))
sum_profit = 0
for i in range(n):
    year_profit = 0
    spam_profit = []
    print()
    name_company = input(f'Введите название {i+1}-го предприятия:')
    for j in range(QUARTERS):
        spam_profit.append(int(input(f'Введите прибыль предприятия "{name_company}" за {j+1}-й квартал:')))
    sum_profit += sum(spam_profit)
    companies[name_company] = spam_profit

print(f'Средняя прибыль за год {sum_profit / n:.2f}')
print('Предприятия с прибылью за год больше средней:')
for i in companies:
    if sum(companies[i]) > sum_profit / n:
        print(i)
print('Предприятия с прибылью за год меньше или равной средней:')
for i in companies:
    if sum(companies[i]) <= sum_profit / n:
        print(i)
