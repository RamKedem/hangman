import hangman
import unittest
from unittest.mock import patch

import random
import string

test = hangman.HangMan('foo')


def random_string(lower_bound=0, upper_bound=5):
    letters = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(letters)
                   for i in range(random.randint(lower_bound, upper_bound)))


class TestHangman(unittest.TestCase):

    def test_check_valid_y_n_answer(self):
        correct_y_replies = {'y', 'Y', 'YES', 'yes', 'Yes', 'yEs'}
        correct_n_replies = {'N', 'n', 'NO', 'no', 'No', 'nO'}

        for reply in correct_y_replies:
            with (patch('builtins.input', return_value=reply)):
                self.assertTrue(test.query_for_yes_no('foo'))
        for reply in correct_n_replies:
            with (patch('builtins.input', return_value=reply)):
                self.assertFalse(test.query_for_yes_no('foo'))

    def test_initially_8_failures_are_allowed(self):
        self.assertEqual(test.number_of_guesses, 8)

    def test_initially_no_letters_are_guessed(self):
        words = [random_string(0,10) for _ in range(10)]
        for word in words:
            game_test = hangman.HangMan(word)
            self.assertEqual(game_test.masked_word,hangman.PLACEHOLDER * len(game_test.chosen_word))

    def test_feeding_a_correct_letter_removes_underscores(self):
        test_game = hangman.HangMan('hello')
        test_game.correct_guess_operations('l')
        self.assertEqual(test_game.masked_word, '--ll-')

if __name__ == '__main__':
    unittest.main()
