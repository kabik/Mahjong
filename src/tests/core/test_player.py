import unittest

from src.core import player

class TestPlayer(unittest.TestCase):
    def test_define(self):
        p = player.Player(0)
        self.assertEqual(p.id, 0)
        self.assertEqual(p.point, 0)

    def test_set_point(self):
        p = player.Player(0)
        p.set_point(1000)
        self.assertEqual(p.point, 1000)

    def test_draw_discard(self):
        p = player.Player(0)
        p.draw(1)
        self.assertEqual(p.hand.main_hand[1], 1)
        p.draw(1)
        self.assertEqual(p.hand.main_hand[1], 2)
        p.discard(1)
        self.assertEqual(p.hand.main_hand[1], 1)
        p.discard(1)
        self.assertEqual(p.hand.main_hand[1], 0)




if __name__ == '__main__':
    unittest.main()
