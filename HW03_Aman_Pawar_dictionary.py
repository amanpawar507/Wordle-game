import random
my_file = open("C:/Users/LENOVO/Desktop/SSW810 Assignments/HW3/words.txt")
file_lines = my_file.read()
dict_list = file_lines.split("\n")
filtered_list = list(filter(lambda l : len(l) == 5 , dict_list))
my_file.close()

def random_word():
    my_word = random.choice(filtered_list)
    return my_word

def is_correct_dict_word(word):
    if word in filtered_list:
        return False
    else:
        print("Input word should be a valid dictionary word")
        return True