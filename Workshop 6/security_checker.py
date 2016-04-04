__author__ = "Jesse Hermon"

usernames = ['jimbo','giltson98','derekf','WhatSup','NicolEye','swei45','BaseInterpreterface',
             'BaseStdIn','Command','ExecState','InteractiveConsole','StartServer','bob']

username_input = input("Username: ")

if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")