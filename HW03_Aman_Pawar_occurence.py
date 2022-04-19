from hashlib import new
from itertools import count
import string


class Occurence:
    dict_lst = {}

    def __init__(self):
        self.dict_lst = {}

    def splt(self, word):
        return [char for char in word]

    def empty_val(self, i):
        if len(i) == 0:
            return True
        else:
            return False

    def occurence_stats(self):
        """This function is used for occurence stats and gives the probability"""
        with open("filter_list_file.txt", "r") as my_file:
            fileLines = my_file.read()
            dictList = fileLines.split("\n")
            x = len(dictList)
            f = open("letterFrequency.csv", "w")
            alphabets = string.ascii_lowercase
            for i in alphabets:
                count_list = [0, 0, 0, 0, 0]
                for key, val in enumerate(dictList):
                    val.lower()
                    splits = self.splt(val)
                    for position, char in enumerate(splits):
                        if char == i:
                            count_list[position] += 1
                self.dict_lst[i] = [round(count_list[0]/x, 3), round(count_list[1]/x, 3), round(
                    count_list[2]/x, 3), round(count_list[3]/x, 3), round(count_list[4]/x, 3)]
            for k, v in self.dict_lst.items():
                f.write("%s:%s\n" % (k, v))
            f.close()
        return self.dict_lst

    def letter_frequency_tuple(self):
        """This function is used for """
        with open("letterFrequency.csv", "r") as mf:
            new_tup = {}
            fileLines = mf.read()
            currentList = fileLines.split("\n")
            for i in currentList:
                if self.empty_val(i):
                    return new_tup
                separated_list = i.split(':')
                keys = separated_list[0]
                res = separated_list[1].strip('][').split(', ')
                new_tup[keys] = tuple(res)
            return new_tup

    def convert_to_tuple(self):
        my_dict = self.occurence_stats()
        new_dict = {}
        for key, value in my_dict.items():
            new_dict[key] = tuple(value)
        return new_dict

    def calc_rank(self):
        """To calculate rank"""
        rank_list = {}
        with open("filter_list_file.txt") as cr:
            value_dict = self.convert_to_tuple()
            fileLines = cr.read()
            currentList = fileLines.split("\n")
            f = open("wordRank.csv", "w")
            for s in currentList:
                if len(s) != 0:
                    weight = 1
                    weight = float(value_dict[s[0]][0])*float(value_dict[s[1]][1])*float(
                        value_dict[s[2]][2])*float(value_dict[s[3]][3])*float(value_dict[s[4]][4])
                    rank_list[s] = format(float(weight), '.15f')
            sorted_list = sorted(rank_list.items(), key=lambda x: x[1])
            sorted_list.reverse()
            count = 0
        for k, v in sorted_list:
            count += 1
            f.write("%s, %s, %s\n" % (count, k, v))

    def __str__(self):
        return f"Occurence(dict_lst:{str(self.dict_lst)})"
