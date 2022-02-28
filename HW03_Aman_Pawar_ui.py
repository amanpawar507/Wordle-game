import HW03_Aman_Pawar_dictionary as dictionary

def get_input(copy_words,x):
    my_word = input("Enter guess #" + str(x+1) + ":")

    #Calling UI functions 
    while letters_5(my_word) or only_chars(my_word) or prev_guesses(my_word, copy_words):
        my_word = input("Enter guess #" + str(x+1) + ":")

    #Calling dictionary functions
    while dictionary.is_correct_dict_word(my_word):
        my_word = input("Enter guess #" + str(x+1) + ":")

    return my_word

def letters_5(word):
    if len(word)==0:
        quit()
    if len(word) != 5:
        print("Input a word with 5 letters only ")
        return True
    else:
        return False

def prev_guesses(my_word, copy_words):
    if my_word in copy_words:
        print("Input should be different than previous guesses")
        return True
    else:
        return False

def only_chars(word):
    if not word.isalpha():
        print("Input should be valid characters only")
        return True
    else:
        return False