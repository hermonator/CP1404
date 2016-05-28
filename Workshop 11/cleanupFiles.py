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
def get_fixed_filename(name):
    print(name)
    if name.find != -1:
        text_array = name.split('_')
        #print(text_array)
        counter = 0
        for i in text_array:
            length_of_word = len(i)
            new_text = ''
            for j in range(0,length_of_word):
                if j == 0:
                    new_text = new_text + i[j].upper()
                else:
                    new_text = new_text + i[j]
                #print(new_text)
            text_array[counter] = new_text
            counter = counter + 1
        #print(text_array)
        new_string =''
        new_string = '_'.join(text_array)
        #text_array = text_array.join()
        #print(new_string)
    else:
        for i in name:
            print(i)
            #if ord(i)


# loop through each file in the (original) directory
for filename in os.listdir('.'):
    # ignore directories, just process files
    if not os.path.isdir(filename):
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
        get_fixed_filename(new_name)
        print(new_name)

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


