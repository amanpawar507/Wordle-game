import unittest
from unittest.mock import patch

import HW03_Aman_Pawar_dictionary as dictionary
import HW03_Aman_Pawar_ui as ui
import HW03_Aman_Pawar_wordle as wordle
import HW03_Aman_Pawar_logger as logger

class WordleTest(unittest.TestCase):

    def test_word_in_dictionary(self) -> None :
        """Testing if dictionary has the given word"""
        self.assertFalse(dictionary.is_correct_dict_word("hello"))

    def test_word_not_in_dictionary(self) -> None :
        """Testing if the dictionary does not have the given word"""
        self.assertTrue(dictionary.is_correct_dict_word("spkdh"))

    def test_input_length_correct(self) -> None :
        """Test when the input word length is correct"""
        self.assertFalse(ui.letters_5("HELLO"))
    
    def test_input_length_incorrect(self) -> None :
        """Test when the input word length is not correct"""
        self.assertTrue(ui.letters_5("CANCER"))

    def test_input_special_characters(self) -> None :
        """Test when the input contains special characters"""
        self.assertTrue(ui.only_chars("@EL@#"))

    def test_input_no_special_characters(self) -> None :
        """Test when the input does not contain special characters"""
        self.assertFalse(ui.only_chars("HELLO"))

    def test_compare_word_function_true(self) -> None :
        """Testing the compare function with correct inputs"""
        self.assertTrue(wordle.compare("HELLO","HELLO"))
    
    def test_compare_word_function_false(self) -> None :
        """Testing the compare function with incorrect inputs"""
        self.assertFalse(wordle.compare("HELLO","BOOKS"))

    def test_input_in_previous_guess(self) -> None :
        """Test when the input word is not correct"""
        self.assertTrue(ui.prev_guesses("BOOKS",["BOOKS"]))
    
    def test_input_not_in_previous_guess(self) -> None :
        """Test when the input word is not correct"""
        self.assertFalse(ui.prev_guesses("BOOKS",["HELLO"]))

    # def test_to_clear_list(self) -> None :
    #     """Test when our random word list has all words from filtererd list file"""
    #     self.assertTrue(wordle.clear_list("BOOKS",["HELLO"]))

    # def test_to_clear_list(self) -> None :
    #     """Test when our random word list does not have all words from filtererd list file"""
    #     self.assertFalse(wordle.clear_list("BOOKS",["HELLO"]))

if __name__ == "__main__":
    unittest.main()

