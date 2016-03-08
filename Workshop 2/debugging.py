__author__ = "Jesse"

score = float(input("Enter score: "))

if score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
elif score > 90 and score < 101:
    print("Excellent")
else:
    print("Invalid score")