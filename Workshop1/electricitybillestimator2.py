__author__ = 'Jesse'

print('Electricity bill estimator 2.0')

tariff = 0

while tariff != 11 | tariff != 31:
    tariff = int(input('Which tariff? 11 or 31:'))
    if tariff != 11 & tariff != 31:
        print("Please enter the correct value:")

hours_daily_usage = float(input('Enter daily use in kWh:'))
number_of_days = float(input('Enter number of billing days:'))
dollars = 0
if tariff == 11:
    dollars = 0.244618
else:
    dollars = 0.136928

bill_costing = 'Estimated bill: $' + str(round((dollars * hours_daily_usage * number_of_days), 2))

print(bill_costing)
