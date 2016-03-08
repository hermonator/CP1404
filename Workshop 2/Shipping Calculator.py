__author__ = "Jesse Hermon"


number_of_items =int(input('Enter the number of items: '))


while number_of_items < 0:
    print("Invaild number of items!")
    number_of_items = int(input('Enter the number of items: '))

shipping_cost_per_item = float(input('Enter the shipping costs: '))
total_shipping_cost = number_of_items * shipping_cost_per_item
if total_shipping_cost > 100:
    total_shipping_cost = total_shipping_cost - (total_shipping_cost * 0.1)

print('The total shipping cost =',total_shipping_cost)