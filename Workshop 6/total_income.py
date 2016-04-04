__author__ = "Jesse Hermon"

incomes = []
months = int(input("How many months? "))

for month in range(1, months + 1):
    income = float(input("Enter income for month {}: ".format(str(month)))) # Change made
    incomes.append(income)

print("\nIncome Report\n-------------")

total = 0
for month in range(1, months + 1):
    income = incomes[month - 1]
    total += income
    print("Month {:2d} - Income: ${:10.2f} Total: ${:10.2f}".format(month,income,total))
