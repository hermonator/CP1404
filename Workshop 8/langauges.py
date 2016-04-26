from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languageslist = [ruby,python,vb]

print("The dynamically typed langauges are:")
for i in range(0,(len(languageslist))):
    if languageslist[i].is_dynamic():
        print(languageslist[i].name)