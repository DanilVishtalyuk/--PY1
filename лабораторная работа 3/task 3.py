money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
balance = money_capital

while True:
    balance += salary
    balance -= spend
    spend = spend * (1 + increase)
    if balance < 0:
        break
    month += 1

print(month)
