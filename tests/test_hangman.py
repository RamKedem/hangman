import hangman
import unittest
import io
import sys

test = hangman.HangMan('hello')

class TestHangman(unittest.TestCase):

    def test_check_valid_guess_in_used_letters(self):
        test.used_letters.add('a')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        test.check_valid_guess('a')
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'You already used that letter')


if __name__ == '__main__':
    unittest.main()
