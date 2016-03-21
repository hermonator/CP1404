__author__ = "Jesse Hermon"

# Constants
MIN_LENGTH_PASSWORD = 3
MAX_LENGTH_PASSWORD = 10
SPECIAL_CHARACTERS = "!@#$%^&*()_=+`~,./'[]\<>?{}|"

# Initial instruction statement
print("""Please enter a valid password\nYour password must be between {0} and {1} characters, and contain:
\t1 or more uppercase characters\n\t1 or more lowercase characters\n\t1 or more numbers
\tand 1 or more special characters:  {2}""".format(MIN_LENGTH_PASSWORD, MAX_LENGTH_PASSWORD, SPECIAL_CHARACTERS))


# Password Valaidity Function
def validityOfPassword(password):
    upper_case_presence = False
    lower_case_presence = False
    special_char_presence = False
    length_of_password = len(password)

    for i in range(length_of_password):
        # print(password[i])

        for j in SPECIAL_CHARACTERS:
            if password[i] == j:
                special_char_presence = True
        if password[i] == password[i].upper() and password[i] not in SPECIAL_CHARACTERS:
            upper_case_presence = True
        elif password[i] == password[i].lower():
            lower_case_presence = True

    result = [upper_case_presence, lower_case_presence, special_char_presence]
    return result


# Main
password = input('>')
valid_password = False
length_of_password = len(password)
# print(length_of_password)

while not valid_password:

    if length_of_password >= MIN_LENGTH_PASSWORD and length_of_password <= MAX_LENGTH_PASSWORD:
        result = validityOfPassword(password)

        if result == [True, True, True]:
            print('Your {} character password is valid: {}'.format(length_of_password, password))
            valid_password = True
        else:
            print("Invalid password!")
            password = input('>')
            length_of_password = len(password)
            # print(length_of_password) check
            # print(result) Check

    else:
        print("Invalid password!")
        password = input('>')
        length_of_password = len(password)
        # print(length_of_password) check
