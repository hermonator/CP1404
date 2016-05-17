from taxi import Taxi, SilverServiceTaxi

def main():

    taxi_list = []
    taxi_list = load_taxis(taxi_list)

    total_fare = 0.00
    fanciness = 1

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_option = input(">>>")
    while menu_option not in ['q','Q']:
        if menu_option in ['c','C']:
            print("Taxis available:")
            display_taxis(taxi_list)
            taxi_input = int(input('Choose taxi: '))

            if taxi_input in [0,1,2]:
                print(end='')

        elif menu_option in ['d','D']:
            drive_distance = int(input('Drive how far? '))
            if taxi_input == 0:
                fanciness = 2.0375
            elif taxi_input == 1:
                fanciness = 1
            elif taxi_input == 2:
                fanciness = 3.59375
            if drive_distance > taxi_list[taxi_input].fuel:
                drive_distance_temp = taxi_list[taxi_input].fuel
            else:
                drive_distance_temp = drive_distance
            taxi_list[taxi_input].drive(drive_distance)

            print("That trip cost you ${:.2f}".format(Taxi.price_per_km *fanciness* drive_distance_temp))
        else:
            print("Invalid option")

        print('Bill to date: ${:.2f}'.format(bill(taxi_list,total_fare,fanciness)))
        # Bill to date statment here
        print("q)uit, c)hoose taxi, d)rive")
        menu_option = input(">>>")
    print("Total trip cost: ${:.2f}".format(bill(taxi_list,total_fare,fanciness)))
    print("Taxis are now:")
    display_taxis(taxi_list)

def display_taxis(taxi_list):


    for i, taxi in enumerate(taxi_list):
        print(i,'-',taxi_list[i])

def load_taxis(taxi_list):

    taxi_list.append(SilverServiceTaxi('Limo',100))
    taxi_list.append(SilverServiceTaxi('Prius',100))
    taxi_list.append(SilverServiceTaxi('Hummer',200))
    return(taxi_list)

def bill(taxi_list,total_fare,fanciness):
    total_fare =0
    for i in range(0,3):
        if i == 0:
            fanciness = 2.0375
        elif i == 1:
            fanciness = 1
        elif i == 2:
            fanciness = 3.59375
        total_fare =total_fare + taxi_list[i].get_fare(fanciness)

    return(total_fare)



main()