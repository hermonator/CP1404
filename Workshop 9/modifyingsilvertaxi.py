from taxi import SilverServiceTaxi

taxi1 = SilverServiceTaxi('Limo',100)
print(taxi1)

print('The initial fare price:',taxi1.get_fare())

taxi1.drive(10)
print(taxi1)

print('The finishing price:',taxi1.get_fare())
