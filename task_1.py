
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

model = LpProblem("Оптимізація виробництва", LpMaximize)

lemonade = LpVariable("Лимонад", lowBound=0, cat='Continuous')
fruit_juice = LpVariable("Фруктовий_сік", lowBound=0, cat='Continuous')

model += lpSum([lemonade, fruit_juice]), "Загальна_кількість"

model += (2 * lemonade + fruit_juice <= 100, "Обмеження_води")
model += (lemonade <= 50, "Обмеження_цукру")
model += (lemonade <= 30, "Обмеження_лимонного_соку")
model += (2 * fruit_juice <= 40, "Обмеження_фруктового_пюре")

model.solve()

print(f"Статус: {LpStatus[model.status]}")
print(f"Кількість лимонаду для виробництва: {value(lemonade)}")
print(f"Кількість фруктового соку для виробництва: {value(fruit_juice)}")
print(f"Максимальна загальна кількість напоїв: {value(model.objective)}")