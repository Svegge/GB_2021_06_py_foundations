'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и 
определите прибыль фирмы в расчете на одного сотрудника.
'''

company_income = float(input('Please submit income value:\n>>> '))
company_costs = float(input('Please submit costs value:\n>>> '))
company_profit = company_income - company_costs

if company_profit > 0:
    print(f'Your company works with profit = {company_profit}')
    print(f'The breakeven is {int(round((company_profit/company_income) * 100, 0))} percent')
    employee_count = int(input('Please enter total quantity of the company employees: '))
    print(f'The profit per employee = {round(company_profit / employee_count, 2)}')
else:
    print(f'Your company has no profit, you lost {company_income - company_costs}')