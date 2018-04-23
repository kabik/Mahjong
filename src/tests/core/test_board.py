import unittest

from src.core import tile
from src.core import player
from src.core import hand
from src.core import board

class TestBoard(unittest.TestCase):
    def test_game_init(self):
        pass

    def test_rest_num_wall(self):
        b = board.Board()
        b.game_init()
        self.assertEqual(b.rest_num_wall(), 70)

    def test_get_next_turn(self):
        b = board.Board()
        b.game_init()
        b.turn = 0
        self.assertEqual(b.get_next_turn(), 1)
        b.turn = 1
        self.assertEqual(b.get_next_turn(), 2)
        b.turn = 2
        self.assertEqual(b.get_next_turn(), 3)
        b.turn = 3
        self.assertEqual(b.get_next_turn(), 0)


if __name__ == '__main__':
    unittest.main()
