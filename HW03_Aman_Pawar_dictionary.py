import random
my_file = open("words.txt", "r")
file_lines = my_file.read()
dict_list = file_lines.split("\n")
filtered_list = list(filter(lambda l : len(l) == 5 , dict_list))
f = open("filter_list_file.txt" , "w")
for listWords in filtered_list:
    f.write(listWords +"\n")
f.close()
my_file.close()

def random_word():
    try:
        myFile = open("filter_list_file.txt", "r")
        fileLines = myFile.read()
        dictList = fileLines.split("\n")
        filteredList=list(dictList)
        my_word = random.choice(filteredList)
        return my_word
    except:
        print("Fatal Error")
        return my_word

def is_correct_dict_word(word):
    if word in filtered_list:
        return False
    else:
        print("Input word should be a valid dictionary word")
        return True