__author__ = "Jesse"

choice = ''

# Practicing defining functions
def printmenu():
    'Prints the menu'
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

name = input("Enter name: ")
printmenu()
choice = input()
loop = 0

while loop == 0:

    if choice == 'H':
        print("Hello "+name)
        printmenu()
    elif choice == 'G':
        print("Goodbye "+name)
        printmenu()
    elif choice == 'Q':
        print('Finished')
        loop = 1
    else:
        print('Invalid choice')
        printmenu()

    choice = input()


