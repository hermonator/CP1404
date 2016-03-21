__author__ = "Jesse Hermon"

name = input("Enter your name: ")
file = open('name.txt', 'w')
print(name, file=file)
file.close()