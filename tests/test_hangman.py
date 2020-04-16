import hangman
import unittest
import random
import string

test = hangman.HangMan('hello')


def random_string(lower_bound=0, upper_bound=5):
    letters = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(letters)
                   for i in range(random.randint(lower_bound, upper_bound)))


class TestHangman(unittest.TestCase):

    def test_check_valid_y_n_answer(self):
        correct_y_replies = {'y', 'Y', 'YES', 'yes', 'Yes', 'yEs'}
        correct_n_replies = {'N', 'n', 'NO', 'no', 'No', 'nO'}
        all_possible_replies = correct_y_replies.union(correct_n_replies)
        wrong_replies = {random_string() for i in range(15)}
        wrong_replies.difference_update(all_possible_replies)

        for reply in correct_y_replies:
            self.assertTrue(test.check_valid_y_n_answer(reply))
        for reply in correct_n_replies:
            self.assertFalse(test.check_valid_y_n_answer(reply))
        for reply in wrong_replies:
            self.assertIsNone(test.check_valid_y_n_answer(reply))

    def test_check_guess_already_used(self):
        guesses = {random_string() for i in range(10)}
        test.used_guesses = guesses
        for guess in guesses:
            self.assertTrue(test.check_guess_already_used(guess))

    def test_check_wrong_guess_already_tried(self):
        guesses = {random_string() for i in range(10)}
        test.wrong_guesses  = guesses
        for guess in guesses:
            self.assertTrue(test.check_wrong_guess_already_tried(guess))

    def test_check_only_one_letter(self):
        guesses = [random_string(1,1) for i in range(10)]
        for guess in guesses:
            self.assertTrue(test.check_only_one_letter(guess))

    def test_check_guess_one_correct_letter(self):
        list_of_words = [random_string(2,10) for i in range(10)]
        for word in list_of_words:
            test.chosen_word = word
            test.g_string = test.chosen_word[random.randint(0,len(word)-1)]
            self.assertTrue(test.check_guess())

    def test_check_guess_one_incorrect_letter(self):
        list_of_words = [random_string(2,10) for i in range(10)]
        for word in list_of_words:
            test.chosen_word = word
            while True:
                test.g_string = random_string(1,1)
                if test.g_string not in test.chosen_word:
                    break
            self.assertFalse(test.check_guess())

    def test_check_guess_correct_word(self):
        list_of_words = [random_string(2, 10) for i in range(10)]
        for word in list_of_words:
            test.g_string = word
            test.chosen_word = word
            self.assertTrue(test.check_guess())

    def test_check_guess_incorrect_word(self):
        list_of_words = [random_string(2, 10) for i in range(10)]
        list_of_wrong_guesses = [word[::-1] for word in list_of_words]
        for ix in range(len(list_of_words)):
            test.g_string = list_of_words[ix]
            test.chosen_word = list_of_wrong_guesses[ix]
            self.assertFalse(test.check_guess())

if __name__ == '__main__':
    unittest.main()
