import HW03_Aman_Pawar_dictionary as dictionary
import HW03_Aman_Pawar_ui as ui
import HW03_Aman_Pawar_logger as logger

#Defining color functions
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

#Printing statistics
def output_stats(played, won, stats):
    print(f"\nGames played: {played}")
    print(f"Win percentage: {(won*100/played): .2f}")  
    for i,game in enumerate(stats):
        print(f"Games won in {i+1} attempt: {game}")

#compare if wordle and given word is same
def compare(x,y):
    if(x==y):
        return True
    else:
        return False

#clear random used word list
def clear_list(usedWords):
    with open("filter_list_file.txt", 'r') as fp:
        x = len(fp.readlines())
        if len(usedWords) == x:
            return True
        else:
            return False

def main():
    gamesPlayed=0
    gamesWon=0
    gameStats = [0] * 6
    while(True):
        
        print("\n**************WORDLE GAME*******************\n")
        print('Each guess must be a valid 5 letter word.\nYou have 6 attempts.\nHit the enter button to submit a word or exit.')

        #Initializing variables
        words = [None] * 6
        copy_words =[None] * 6
        try:
            myWord = dictionary.random_word().upper()
        except:
            print("")
        print(myWord)
        used_words = []
        used_words.append(myWord.lower())
        if clear_list(used_words):
            used_words.clear() 
        #Loop for 6 times for 6 attempts
        for x in range(6):
            #variables for storing abbreviations
            final_list = [None] * 5
            final_string = ""

            #Creating copy of input words 
            copy_words = words.copy()
            
            #Taking input
            print("\nGuess the word")
            words[x] = ui.get_input(copy_words, x)
            copy_myWord = myWord
            #Check if the word was correct
            if (compare(words[x].upper(), myWord)):
                prGreen("Correct guess, You win!")
                gameStats[x] += 1
                gamesWon += 1
                break
            else:
                print(words[x].upper())
                #Looping to check each letter
                for y in range(5):
                    #Check which letter is in correct position and is a correct word
                    if words[x][y].upper() == copy_myWord[y]:
                        i = y
                        copy_myWord =  copy_myWord[:i] +" "+ copy_myWord[i+1:]
                        final_list[y] = " "
                        
                for y in range(5):   
                    if(final_list[y] != None):
                        continue
                    else:
                        #Check which letter is correct but in wrong position
                        if words[x][y].upper() in copy_myWord:
                            my_letter = words[x][y].upper()
                            i= int(copy_myWord.find(my_letter))
                            copy_myWord =  copy_myWord[:i] +" "+ copy_myWord[i+1:]
                            final_list[y] = "`"
                        
                        #Check if the letter is incorrect  
                        else: 
                            final_list[y] = '"'
                            continue
                
                for i in final_list:
                    final_string += str(i) + ""
                print(final_string)

                #Exit when all attempts are exhausted
                if x==5: prRed("You lose!")
                continue    
        gamesPlayed+=1
        try:
            output_stats(gamesPlayed, gamesWon, gameStats)
        except:
            print("Fatal error: annot output statistics")
        try:
            logger.log_writer(myWord, words, gamesPlayed, gamesWon, gameStats)
        except:
            print("Error: Cannot update logs")
        
if __name__== "__main__":
    main()