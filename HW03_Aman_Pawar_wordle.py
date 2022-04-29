import HW03_Aman_Pawar_dictionary as dictionary
import HW03_Aman_Pawar_ui as ui
import HW03_Aman_Pawar_logger as logger
import HW03_Aman_Pawar_occurence as occurence


class Main:
    gamesPlayed = 0
    gamesWon = 0
    gameStats = []

    def __init__(self):
        self.d = dictionary.Dictionary()
        self.u = ui.Ui()
        self.o = occurence.Occurence()
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.gameStats = [0] * 6

    def __str__(self):
        return f"Main(gamesPlayed:{str(self.gamesPlayed)}, gamesWon:{str(self.gamesWon)}, gameStats:{str(self.gameStats)})"

    # Printing statistics
    def output_stats(self, played, won, stats):
        print(f"\nGames played: {played}")
        print(f"Win percentage: {(won*100/played): .2f}")
        for i, game in enumerate(stats):
            print(f"Games won in {i+1} attempt: {game}")

    # compare if wordle and given word is same
    def compare(self, x, y):
        if(x == y):
            return True
        else:
            return False

    # clear random used word list
    def clear_list(self, usedWords):
        with open("filter_list_file.txt", 'r') as fp:
            x = len(fp.readlines())
            if len(usedWords) == x:
                return True
            else:
                return False

    def solverHelper(self, myWord, x, initialGuess, my_db_logger):
        # variables for storing abbreviations
        final_list = [None] * 5
        final_string = ""
        # Taking input
        words = [None]*6
        words[x] = initialGuess
        if words[x] == None:
            quit()
        my_db_logger.insert_to_details(
            attempt=x+1, wordle=myWord, input_word=initialGuess)
        copy_myWord = myWord
        # Check if the word was correct
        if (self.compare(words[x].upper(), myWord)):
            print("Correct guess, You win!")
            self.gameStats[x] += 1
            self.gamesWon += 1
            return "Wordle found"
        else:
            print(words[x].upper())
            # Looping to check each letter
            for y in range(5):
                # Check which letter is in correct position and is a correct word
                if words[x][y].upper() == copy_myWord[y]:
                    i = y
                    copy_myWord = copy_myWord[:i] + " " + copy_myWord[i+1:]
                    final_list[y] = " "

            for y in range(5):
                if(final_list[y] != None):
                    continue
                else:
                    # Check which letter is correct but in wrong position
                    if words[x][y].upper() in copy_myWord:
                        my_letter = words[x][y].upper()
                        i = int(copy_myWord.find(my_letter))
                        copy_myWord = copy_myWord[:i] + " " + copy_myWord[i+1:]
                        final_list[y] = "`"

                    # Check if the letter is incorrect
                    else:
                        final_list[y] = '"'
                        continue

            for i in final_list:
                final_string += str(i) + ""
            print(final_string)

            # Exit when all attempts are exhausted
            if x == 5:
                print("You lose!")
            return final_string

    def game(self, words, x, myWord):
        # variables for storing abbreviations
        final_list = [None] * 5
        final_string = ""

        # Creating copy of input words
        copy_words = words.copy()

        # Taking input
        print("\nGuess the word")

        words[x] = self.u.get_input(copy_words, x)
        if words[x] == None:
            quit()

        copy_myWord = myWord
        # Check if the word was correct
        if (self.compare(words[x].upper(), myWord)):
            print("Correct guess, You win!")
            self.gameStats[x] += 1
            self.gamesWon += 1
            return "Wordle found"
        else:
            print(words[x].upper())
            # Looping to check each letter
            for y in range(5):
                # Check which letter is in correct position and is a correct word
                if words[x][y].upper() == copy_myWord[y]:
                    i = y
                    copy_myWord = copy_myWord[:i] + " " + copy_myWord[i+1:]
                    final_list[y] = " "

            for y in range(5):
                if(final_list[y] != None):
                    continue
                else:
                    # Check which letter is correct but in wrong position
                    if words[x][y].upper() in copy_myWord:
                        my_letter = words[x][y].upper()
                        i = int(copy_myWord.find(my_letter))
                        copy_myWord = copy_myWord[:i] + " " + copy_myWord[i+1:]
                        final_list[y] = "`"

                    # Check if the letter is incorrect
                    else:
                        final_list[y] = '"'
                        continue

            for i in final_list:
                final_string += str(i) + ""
            print(final_string)

            # Exit when all attempts are exhausted
            if x == 5:
                print("You lose!")
            return final_string

    def main(self):

        while(True):

            print("\n**************WORDLE GAME*******************\n")
            print('Each guess must be a valid 5 letter word.\nYou have 6 attempts.\nHit the enter button to submit a word or exit.')

            # Initializing variables
            words = [None] * 6
            copy_words = [None] * 6
            try:
                myWord = self.d.random_word().upper()
            except:
                print("Error")
            print(myWord)
            used_words = []
            used_words.append(myWord.lower())
            if self.clear_list(used_words):
                used_words.clear()
            # Loop for 6 times for 6 attempts

            for x in range(6):
                stringReturned = self.game(words, x, myWord)
                if(stringReturned == "Wordle found"):
                    break
                else:
                    continue

            self.gamesPlayed += 1
            try:
                self.output_stats(self.gamesPlayed,
                                  self.gamesWon, self.gameStats)
            except:
                print("Fatal error: annot output statistics")
            try:
                logger.log_writer(myWord, words, self.gamesPlayed,
                                  self.gamesWon, self.gameStats)
            except:
                print("Error: Cannot update logs")


if __name__ == "__main__":
    w = Main()
    w.main()
