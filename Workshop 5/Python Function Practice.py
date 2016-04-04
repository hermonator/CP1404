__author__ = "Jesse Hermon"

#### Function that calculates the area of a rectangle
def area_of_a_rectangle():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    print(area)


#### Converts Celcius to Fahrenheit
def celcuis_to_Fahrenheit():
    celcuis = float(input("Enter the celcuis value: "))
    fahrenheit = celcuis * 1.8 + 32
    print(fahrenheit)

#### Calculating Body Mass Index
def body_Mass_Index():
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    bmi = weight / (height/100)**2
    print(bmi)

area_of_a_rectangle()
celcuis_to_Fahrenheit()
body_Mass_Index()
