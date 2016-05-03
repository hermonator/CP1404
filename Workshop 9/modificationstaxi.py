from taxi import Taxi

def main():


    # Step 1
    # taxi1 =Taxi('Prius 1',100,1.20)

    # Step 5
    taxi1 = Taxi('Prius 1',100)

    #   Check
    #   print(taxi1)

    # Step 2
    taxi1.drive(40)
    print(taxi1)

    # Step 3
    taxi1.odometer = 0
    taxi1.drive(100)

    #   Check
    #   print(taxi1)

    # step 4
    print(taxi1)


main()