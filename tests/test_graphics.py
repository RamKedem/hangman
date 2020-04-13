import unittest
import graphics

GRAPHICS = list(graphics.hang_graphics())

class TestGraphics(unittest.TestCase):

    def test_len_hang_graphics(self):
        self.assertEqual(len(GRAPHICS),8)

    def test_values_hang_graphics(self):
        for c,graphic in enumerate(GRAPHICS):
            self.assertIsNotNone(graphic)


if __name__ == '__main__':
    unittest.main()


