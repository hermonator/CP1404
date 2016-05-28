"""
CP1404 Workshop code - file renaming
"""
import os, shutil

__author__ = 'Lindsay Ward'

# change to desired directory
os.chdir('Lyrics/Christmas')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
# os.mkdir('temp')

# loop through each file in the (original) directory
for filename in os.listdir('.'):
    # ignore directories, just process files
    if not os.path.isdir(filename):
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")


        # Check for uppercase characters after the current characters
        new_name_check2 = ''
        #print(len(new_name))
        for i in range(len(new_name) - 1):
            #print(new_name[i+1])
            #print(new_name[i-1])
            if i >= 1:
                if new_name[i + 1] == new_name[i + 1].upper() and new_name[i + 1] not in ['_',' ','.',')'] and new_name_check2[-1] != '_' and new_name[i] != '_':
                    new_name_check2 = new_name_check2 + new_name[i] + '_'
                else:
                    new_name_check2 = new_name_check2 + new_name[i]
            else:
                if new_name[i + 1] == new_name[i + 1].upper() and new_name[i + 1] != '_':
                    new_name_check2 = new_name_check2 + new_name[i] + '_'
                else:
                    new_name_check2 = new_name_check2 + new_name[i]
        new_name_check2 = new_name_check2 + 't'

        #print(new_name_check2)

        # Changing words to capital case
        new_name_check3 = ''
        post_underscore = 0
        for i in range(len(new_name_check2) -1):

            if post_underscore == 1:
                new_name_check3 = new_name_check3 + new_name_check2[i].upper()
                post_underscore = 0
            else:
                new_name_check3 = new_name_check3 + new_name_check2[i]
            if new_name_check2[i] == '_':
                post_underscore = 1
        new_name_check3 = new_name_check3 + 't'

        print(new_name_check3)

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)


