__author__ = "Jesse Hermon"

COLOUR_CODES = {"aquamarine1":"#7fffd4","black":"#000000","blue1":"#0000ff","BlueViolet":"#8a2be2","brown1":"#ff4040",
               "CadetBlue1":"#98f5ff","chartreuse1":"#7fff00","chocolate1":"#ff7f24","cyan":"#00ffff","DarkOrange":"#ff8c00"}
# print(STATE_NAMES)

colour = input("Enter a colour: ")
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is",COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ")