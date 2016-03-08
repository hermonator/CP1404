__author__ = 'Jesse'

print('Electricity bill estimator')

cents = float(input('Enter cents per kWh:'))
hours_daily_usage = float(input('Enter daily use in kWh:'))
number_of_days = float(input('Enter number of billing days:'))

bill_costing = 'Estimated bill: $' + str(cents * hours_daily_usage * number_of_days / 100)

print(bill_costing)