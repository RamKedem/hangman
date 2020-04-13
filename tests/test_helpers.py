import helpers
import unittest


class TestHelpers(unittest.TestCase):

    def test_valid_n(self):
        valid_n_replys = ['N','n']
        for reply in valid_n_replys:
            result = helpers.check_valid_y_n_answer('N')
            self.assertFalse(result)

    def test_valid_y(self):
        valid_y_replys = ['Y','y']
        for reply in valid_y_replys:
            result = helpers.check_valid_y_n_answer('Y')
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
