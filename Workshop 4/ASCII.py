__author__="Jesse Hermon"

lower = int(input("Enter the bottom of the range: ").strip())
upper = int(input("Enter the top of the range: ").strip())


# Rewrite the cumbersome print line to use nice string formatting with the format method.
# print("Enter a number (" +str(lower) + "-" + str(upper) + "):")
print("Enter a number {0}-{1}".format(lower, upper))

for i in range(lower, upper, 1):
    if i >= 32:
        print("|{} | {}|".format(i, chr(i)))
        print("--------")