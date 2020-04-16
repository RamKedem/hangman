import generate_words
import unittest

TEST_SOURCE = '../'+ generate_words.SOURCE


class TestGenerateWords(unittest.TestCase):

    def test_generate_strings_only(self, source=TEST_SOURCE):
        with open(source, 'r') as f:
            for word in f:
                self.assertTrue(word.strip('\n').isalpha())

    def test_generate_words_with_valid_len(self, source=TEST_SOURCE):
        with open(source, 'r') as f:
            for word in f:
                self.assertGreater(len(word.strip('\n')), 1)
                

if __name__ == '__main__':
    unittest.main()
