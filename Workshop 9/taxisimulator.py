from taxi import Taxi, SilverServiceTaxi

def main():

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_option = input(">>>")
    while menu_option not in ['q','Q']:
        if menu_option in ['c','C']:
            print('dill')
        elif menu_option in ['d','D']:
            print('gfji')
        else:
            print("Invalid option")
        # Bill to date statment here
        print("q)uit, c)hoose taxi, d)rive")
        menu_option = input(">>>")

    # print trip costs
    # print taxi's current details

def display_taxis():



main()