
print("\n**************WORDLE GAME*******************\n")
print('Each guess must be a valid 5 letter word.\nYou have 6 attempts.\nHit the enter button to submit.')

#Defining color functions
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#Initializing variables
words = [None] * 6
copy_words =[None] * 6
myWord = "SONAR"

#Loop for 6 times for 6 attempts
for x in range(6):

    #Creating copy of input words 
    copy_words = words.copy()
    
    #Taking input
    print("\nGuess the word")
    words[x] = input("Enter guess #" + str(x+1) + ":")

    #Validation checks for input
    while len(words[x]) != 5 or not words[x].isalpha():
        print("Input a word with 5 letters only and should be valid characters only")
        words[x] = input("Enter guess #" + str(x+1) + ":")
    while words[x] in copy_words:
        print("Input should be different than previous guesses")
        words[x] = input("Enter guess #" + str(x+1) + ":")

    #Check if the word was correct
    if (words[x].upper()==myWord):
        prGreen("Correct guess, You win!")
        quit()
    else:
        letter=0
        #Looping to check each letter
        for y in range(len(words[x])):
            #Check which letter is in correct position and is a correct word
            if words[x][letter].upper() == myWord[letter]:
                prGreen(str(words[x][letter].upper())+ " -> correct spot")
                letter += 1 
            #Check which letter is correct but in wrong position
            elif words[x][letter].upper() in myWord:
                prYellow(str(words[x][letter].upper()) + " -> incorrect spot")
                letter += 1 
            #Chheck if the letter is incorrect  
            else: 
                prRed(str(words[x][letter].upper()) + " -> not in any spot")
                letter += 1 
                continue 
        #Exit when all attempts are exhausted
        if x==5: prRed("You lose!")
        continue
    
"""
Pseudocode:

DEFINE COLOR FUNCTIONS
INITIALIZE words,copy_words TO EMPTY ARRAY OF SIZE 6
SET myWord TO "SONAR"

ITERATE ATTEMPTS IN range(6): 
    SET copy_words TO words.copy
    DISPLAY "Guess the word"
    SET words[x] TO INPUT("Enter INPUT #" + str(x+1) + ":") FROM USER

    WHILE LENGTH(words[x]) != 5 OR words[x] IS NOT ALPHABETS:
        DISPLAY "Input a word with 5 letters only and should be valid characters only"
        SET words[x] TO INPUT ("Enter INPUT #" + str(x+1) + ":") FROM USER
    WHILE words[x] IN copy_words:
        DISPLAY "Input should be differet than previous guesses"
        SET words[x] TO INPUT ("Enter INPUT #" + str(x+1) + ":") FROM USER

    IF words[x].upper EQUALS myWord:
        DISPLAY "Correct guess, You win!" IN GREEN
        QUIT
    ELSE:
        letter=0
        ITERATE LETTERS IN range(len(words[x])):
            IF words[x][letter].upper EQUALS myWord[letter]:
                DISPLAY str(words[x][letter].upper) + " -> correct spot" IN GREEN
                INCREMENT letter BY 1 
            ELSEIF words[x][letter].upper() IN myWord:
                DISPLAY str(words[x][letter].upper) +"-> incorrect spot" IN YELLOW
                INCREMENT letter BY 1 
            ELSE: 
                DISPLAY str(words[x][letter].upper) + "-> not IN any spot" IN RED
                INCREMENT letter BY 1 
                CONTINUE

        IF x EQUALS 5: 
            DISPLAY "You lose!" IN RED
        CONTINUE
"""