money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
k = 0
while money_capital + salary >= spend:
    k = k + 1
    money_capital = money_capital + salary - spend
    spend = spend + spend * increase
#    print(money_capital, spend)
#    print()
print("Количество месяцев, которое можно протянуть без долгов:", k)