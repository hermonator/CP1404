__author__ = "Jesse Hermon"

text =input("Text: ")
words = sorted(text.split())

# print(words)
word_dict ={}

for i in (words):
    if i not in word_dict:
        word_dict[i] = 1
    else:
        counter = word_dict[i] + 1
        word_dict[i] = counter


for i in sorted(word_dict):
    print("{} : {}".format(i,word_dict[i]))
    # print(i)

#print(sorted(word_dict))
#print(sorted_list)