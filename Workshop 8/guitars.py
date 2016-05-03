__author__ = "Jesse Hermon"

from guitar import Guitar

def main():

    print('My guitars!')

    # A control structure to input and store the users guitars.
    guitars_list = []
    guitar_name ='a'
    #guitar_counter = 0
    #guitar_title = 'Guitar '
    while guitar_name != '':
        guitar_name = input('Name: ')
        if guitar_name != '':
            #guitar_counter = guitar_counter + 1
            guitar_year = int(input('Year: '))
            guitar_cost = float(input('Cost: '))
            guitars_list.append(Guitar(guitar_name,guitar_year,guitar_cost))
            print('{} added'.format(guitars_list[-1]))

            
    # A control structure to display the guitars.
    for i, guitar in enumerate(guitars_list):

        vintage_string = ''
        if guitar.is_vintage():
            vintage_string = '(vintage)'

        print('Guitar {}: {:>20} ({}), worth ${:10,.2f} {}'.format(i + 1, guitar.name,guitar.year,guitar.cost,vintage_string))





main()
