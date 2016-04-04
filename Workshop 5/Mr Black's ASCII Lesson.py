__author__="Jesse Hermon"

# Function for getting the lower and upper inputs
def get_number():
    valid_inputs = False
    while not valid_inputs:
        try:
            lower = int(input("Enter the bottom of the range: ").strip())
            upper = int(input("Enter the top of the range: ").strip())
            if lower >= 32:
                if upper <= 126:
                    if upper > lower:
                        valid_inputs = True
                    else:
                        print("The upper limit is required to be higher than the lower limit.")
                else:
                    print("The upper limit is required to be less than or equal to 126.")
            else:
                print("The lower limit is require to be greater than or equal to 32.")

        except ValueError:
            print("Not a valid integer")

    return lower,upper

# Rewrite the cumbersome print line to use nice string formatting with the format method.
# print("Enter a number (" +str(lower) + "-" + str(upper) + "):")
lower,upper = get_number()
print("Enter a number {0}-{1}".format(lower, upper))

for i in range(lower, upper, 1):
    if i >= 32:
        print("|{} | {}|".format(i, chr(i)))
        print("--------")