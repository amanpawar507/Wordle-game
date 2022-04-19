import unittest
from unittest.mock import patch

from HW03_Aman_Pawar_dictionary import Dictionary as dictionary
from HW03_Aman_Pawar_ui import Ui as ui
from HW03_Aman_Pawar_wordle import Main as wordle
from HW03_Aman_Pawar_occurence import Occurence as occurence


class WordleTest(unittest.TestCase):
    # def __init__(self):
    #     self.d = dictionary.Dictionary()
    #     self.u = ui.Ui()
    #     self.w = wordle.Main()

    def test_word_in_dictionary(self) -> None:
        """Testing if dictionary has the given word"""
        di = dictionary()
        self.assertFalse(di.is_correct_dict_word("hello"))

    def test_word_not_in_dictionary(self) -> None:
        """Testing if the dictionary does not have the given word"""
        di = dictionary()
        self.assertTrue(di.is_correct_dict_word("spkdh"))

    def test_input_length_correct(self) -> None:
        """Test when the input word length is correct"""
        uu = ui()
        self.assertFalse(uu.letters_5("HELLO"))

    def test_input_length_incorrect(self) -> None:
        """Test when the input word length is not correct"""
        uu = ui()
        self.assertTrue(uu.letters_5("CANCER"))

    def test_input_special_characters(self) -> None:
        """Test when the input contains special characters"""
        uu = ui()
        self.assertTrue(uu.only_chars("@EL@#"))

    def test_input_no_special_characters(self) -> None:
        """Test when the input does not contain special characters"""
        uu = ui()
        self.assertFalse(uu.only_chars("HELLO"))

    def test_compare_word_function_true(self) -> None:
        """Testing the compare function with correct inputs"""
        wo = wordle()
        self.assertTrue(wo.compare("HELLO", "HELLO"))

    def test_compare_word_function_false(self) -> None:
        """Testing the compare function with incorrect inputs"""
        wo = wordle()
        self.assertFalse(wo.compare("HELLO", "BOOKS"))

    def test_input_in_previous_guess(self) -> None:
        """Test when the input word is not correct"""
        uu = ui()
        self.assertTrue(uu.prev_guesses("BOOKS", ["BOOKS"]))

    def test_input_not_in_previous_guess(self) -> None:
        """Test when the input word is not correct"""
        uu = ui()
        self.assertFalse(uu.prev_guesses("BOOKS", ["HELLO"]))

    def test_to_clear_list(self) -> None:
        """Test when our random word list has all words from filtererd list file"""
        wo = wordle()
        self.assertFalse(wo.clear_list(["HELLO", "BOOKS"]))

    def test_to_check_empty(self) -> None:
        """Test when it is an empty element"""
        oc = occurence()
        self.assertTrue(oc.empty_val(""))

    def test_to_check_not_empty(self) -> None:
        """Test when it is not empty"""
        oc = occurence()
        self.assertFalse(oc.empty_val("aaron"))


if __name__ == "__main__":
    unittest.main()
