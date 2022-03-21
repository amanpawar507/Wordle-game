import HW03_Aman_Pawar_dictionary as dictionary

class Ui:
    my_word = ""
    def __init__(self):
        self.di = dictionary.Dictionary()
        self.my_word = ""

    def get_input(self, copy_words, x):
        try:
            self.my_word = input("Enter guess #" + str(x+1) + ":")
            #Calling UI functions 
            if self.exit_game(self.my_word):
                return None

            while self.letters_5(self.my_word) or self.only_chars(self.my_word) or self.prev_guesses(self.my_word, copy_words):
                self.my_word = input("Enter guess #" + str(x+1) + ":")

            #Calling dictionary functions
            while self.di.is_correct_dict_word(self.my_word):
                self.my_word = input("Enter guess #" + str(x+1) + ":")

            return self.my_word
        except:
            print("I/O Error")

    def get_my_word(self):
        return self._my_word

    def letters_5(self, word):
        if len(word) != 5 and len(word)>0:
            print("Input a word with 5 letters only ")
            return True
        else:
            return False

    def prev_guesses(self, my_word, copy_words):
        if my_word in copy_words:
            print("Input should be different than previous guesses")
            return True
        else:
            return False

    def only_chars(self, word):
        if not word.isalpha():
            print("Input should be valid characters only")
            return True
        else:
            return False

    def exit_game(self, word):
        if len(word) == 0:
            return True
        else:
            return False

    def __str__(self):
        return f"Ui(my_word:{str(self.my_word)})"