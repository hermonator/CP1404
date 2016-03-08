__author__ = 'Jesse Hermon'

x = int(input('Enter x: '))
y = int(input('Enter y: '))

def printmenu():
    print("\n\t1.Show the even numbers from x to y")
    print("\t2.Show the odd numbers from x to y")
    print("\t3.Show the squares from x to y")
    print("\t4.Exit the program\n")

loop = 0

while loop == 0:
    printmenu()
    menuinput = input('Enter the menu option: ')
    if menuinput == '1':
        if x % 2 == 1:
            x = x + 1
            for i in range(x, y, 2):
                print(i, end = ' ')
            x = x - 1
        else:
            for i in range(x, y, 2):
                print(i, end = ' ')
    elif menuinput == '2':
        if x % 2 == 0:
            x = x + 1
            for i in range(x, y, 2):
                print(i, end = ' ')
            x = x - 1
        else:
            for i in range(x, y, 2):
                print(i, end = ' ')
    elif menuinput == '3':
        for i in range(x, y, 1):
                print((i**i), end = ' ')
    elif menuinput == '4':
        print('Goodbye')
        loop = 1
    else:
        print('Invaild option')
    
    








