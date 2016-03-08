__author__ = "Jesse Hermon"

my_file = open("wordsEn.txt", "r")

for line_str in my_file:
    char_counter = 0
    line_str = line_str.strip()
    for char in line_str:
        #if char == 'a' and char_counter > 0:
         #   char_counter = 6
        if char == 'a' and char_counter == 0:
            char_counter = char_counter + 1
        elif char == 'e' and char_counter == 1:
            char_counter = char_counter + 1
        elif char == 'i' and char_counter == 2:
            char_counter = char_counter + 1
        elif char == 'o' and char_counter == 3:
            char_counter = char_counter + 1
        elif char == 'u' and char_counter == 4:
            char_counter = char_counter + 1
       # elif char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            #char_counter = 6
        if char_counter == 5:

            print(line_str)
            char_counter = char_counter + 1


        #else:
            #print('nope')
    if char_counter == 6:
        break



