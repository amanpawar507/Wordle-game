import HW03_Aman_Pawar_helper as helper
import HW03_Aman_Pawar_wordle as wordle
import random


class Solver:

    words = []

    def __init__(self):
        self.words = []
        self.myMain = wordle.Main()
        self.helps = helper.Helper()

    def convert(self, s):
        # initialization of string to ""
        str1 = ""

        # using join function join the list s by
        # separating words by str1
        return(str1.join(s))

    def mySolver(self):

        f = open("filter_list_file.txt")
        self.words = f.read().split("\n")
        solution = list(self.words[random.randint(0, 1378)].upper())
        myWordle = self.convert(solution).lower()
        attempts = 0
        #self.myMain.game(self.words, 0, solution)

        goodLetters = []
        badLetters = []
        index0 = ""
        index1 = ""
        index2 = ""
        index3 = ""
        index4 = ""

        initialGuess = "sales"
        guesslist = []
        print("The answer for this round is", myWordle)
        print()

        while attempts < 6:
            print(f'Guess #{attempts+1}')
            print("My guess is", initialGuess)
            try:
                result = self.myMain.solverHelper(
                    myWordle.upper(), attempts, initialGuess.upper())
            except:
                print("Not found")

            if result == "Wordle found":
                print(f"You win! Your word is {initialGuess}")
                break

            for i in range(5):
                if result[i] == " " and i == 0:
                    index0 = initialGuess[i]

                elif result[i] == " " and i == 1:
                    index1 = initialGuess[i]

                elif result[i] == " " and i == 2:
                    index2 = initialGuess[i]

                elif result[i] == " " and i == 3:
                    index3 = initialGuess[i]

                elif result[i] == " " and i == 4:
                    index4 = initialGuess[i]

                elif result[i] == "'":
                    goodLetters.append(initialGuess[i])

            for i in range(5):
                if result[i] == '"' and initialGuess[i] not in goodLetters and initialGuess[i] != index0 and initialGuess[i] != index1 and initialGuess[i] != index2 and initialGuess[i] != index3 and initialGuess[i] != index4:
                    badLetters.append(initialGuess[i])

            attempts = attempts + 1
            guesslist.append(initialGuess)
            print()
            initialGuess = self.helps.rankedWords(goodLetters, badLetters)
            if initialGuess == None:
                print("Failed to solve the Wordle \n")
                break


myRun = Solver()
myRun.mySolver()
