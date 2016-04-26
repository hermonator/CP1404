from car import Car

def main():

    ### Given syntax
    bus  =  Car(180)
    bus.drive(30)
    print("fuel  =",  bus.fuel)
    print("odo  =",  bus.odometer)
    print(bus)

    ### Modifcations

    # Step 1
    limo = Car("limo",100)
    print("Limo has {}L of fuel".format(limo.fuel))
    # Step 2
    limo.fuel += 20
    # Step 3
    print("Limo has {}L of fuel".format(limo.fuel))
    # Step 4
    limo.drive(115)
    # Step 5
    print("Limo's odometer reads {}".format(limo.odometer))
    # Step 6
    print(limo)
    # Step 7



main()