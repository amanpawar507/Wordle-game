import string

def split(word):
    return [char for char in word]
     
# Driver code
# word = 'geeks'
# print(split(word))

def occurence_stats():
    with open("filter_list_file.txt", "r") as my_file:
        fileLines = my_file.read()
        dictList = fileLines.split("\n")
        x = len(dictList)
        f = open("letterFrequency.csv" , "w")
        alphabets = string.ascii_lowercase
        for i in alphabets:
            count_list = [0,0,0,0,0]
            for key,val in enumerate(dictList):
                val.lower()
                splits = split(val)
                for position,char in enumerate(splits):
                    if char == i:
                        count_list[position] += 1
            f.write(f"{i},{round(count_list[0]/x, 3)},{round(count_list[1]/x, 3)},{round(count_list[2]/x, 3)},{round(count_list[3]/x, 3)},{round(count_list[4]/x, 3)}\n")
            #f.write(splits)
        f.close()
                
# def letter_frequency_tuple():
#     with open("letterFrequency.csv", "r") as mf:
#         fileLines = mf.read()
#         currentList = fileLines.split("\n")
#         for i in currentList:
#             separated_list = i.split(',')
#             frequency_tuple = tuple(separated_list)
#             print(frequency_tuple)
