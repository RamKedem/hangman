import hangman
import unittest
import io
import sys

test = hangman.HangMan('hello')

class TestHangman(unittest.TestCase):

    def test_check_valid_guess_in_used_letters(self):
        pass

if __name__ == '__main__':
    unittest.main()
