import unittest
import graphics

GRAPHICS = list(graphics.hang_graphics())

class TestGraphics(unittest.TestCase):

    def test_len(self):
        self.assertEqual(len(GRAPHICS),8)

    def test_for_non_empty_values(self):
        for c,graphic in enumerate(GRAPHICS):
            self.assertIsNotNone(graphic)


if __name__ == '__main__':
    unittest.main()


