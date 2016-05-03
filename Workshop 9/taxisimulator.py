from taxi import Taxi, SilverServiceTaxi

def main():

    load_taxis()
    display_taxis()
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
        print('Bill to date: $',get_fare())
        # Bill to date statment here
        print("q)uit, c)hoose taxi, d)rive")
        menu_option = input(">>>")

    # print trip costs
    # print taxi's current details

def display_taxis():

    #for i, guitar in enumerate(guitars_list):

     #   vintage_string = ''
      #  if guitar.is_vintage():
       #     vintage_string = '(vintage)'

        print(SilverServiceTaxi(Limo))


def load_taxis():

    SilverServiceTaxi('Limo',100)
    SilverServiceTaxi('Prius',100)
    SilverServiceTaxi('Hummer',200)



main()