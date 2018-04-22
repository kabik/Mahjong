import unittest

from src.core import tile
from src.core import hand

class TestHand(unittest.TestCase):
    def test_constructor(self):
        h = hand.Hand(0)
        self.assertEqual(h.id, 0)
        self.assertEqual(len(h.main_hand), 37)
        h.main_hand[1] = 1
        self.assertIs(h.main_hand[1] == hand.empty_tile_set[1], False)
        self.assertEqual(len(h.open_sets), 4)

    def test_empty_tile_set(self):
        for n in hand.empty_tile_set:
            self.assertEqual(n, 0)
        self.assertEqual(len(hand.empty_tile_set), 37)

    def test_can_win(self):
        pass

    def test_can_pong(self):
        h = hand.Hand(0)
        h.main_hand[1] = 1
        self.assertIs(h.can_pong(1), False)
        h.main_hand[1] = 2
        self.assertIs(h.can_pong(1), True)
        h.main_hand[1] = 3
        self.assertIs(h.can_pong(1), True)

    def test_can_chow(self):
        h = hand.Hand(0)
        h.main_hand = [0,0,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,0,1,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,
                       0,1,1,0,1,0,0]
        self.assertIs(h.can_chow(1), True)
        self.assertIs(h.can_chow(2), False)
        self.assertIs(h.can_chow(6), True)
        self.assertIs(h.can_chow(8), False)
        self.assertIs(h.can_chow(9), True)
        self.assertIs(h.can_chow(15), True)
        self.assertIs(h.can_chow(30), False)
        self.assertIs(h.can_chow(33), False)

    def test_can_daiminkan(self):
        h = hand.Hand(0)
        h.main_hand[1] = 2
        self.assertIs(h.can_ankan(1), False)
        h.main_hand[1] = 3
        self.assertIs(h.can_ankan(1), True)

    def test_can_kakan(self):
        h = hand.Hand(0)
        h.open_sets[0][1] = 1
        self.assertIs(h.can_kakan(1), False)
        h.open_sets[0][1] = 3
        self.assertIs(h.can_kakan(1), True)

    def test_can_ankan(self):
        h = hand.Hand(0)
        h.main_hand[1] = 2
        self.assertIs(h.can_ankan(1), False)
        h.main_hand[1] = 3
        self.assertIs(h.can_ankan(1), True)

    def test_claim(self):
        h = hand.Hand(0)
        h.main_hand = [0,0,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,0,1,0,0,0,
                       0,0,2,0,0,0,0,0,0,0,
                       0,3,1,0,1,0,0]

        # chow
        h.claim([2,3], 4, 1)
        self.assertEqual(h.main_hand[2],0)
        self.assertEqual(h.main_hand[3],0)
        self.assertEqual(h.open_sets[0][2], 1)
        self.assertEqual(h.open_sets[0][3], 1)
        self.assertEqual(h.claimed_tile[0], 4)
        self.assertEqual(h.claimed_player[0], 1)

        # pong
        h.claim([22,22], 22, 2)
        self.assertEqual(h.main_hand[22],0)
        self.assertEqual(h.open_sets[1][22], 2)
        self.assertEqual(h.claimed_tile[1], 22)
        self.assertEqual(h.claimed_player[1], 2)

        # kan
        h.claim([31,31,31], 31, 3)
        self.assertEqual(h.main_hand[31],0)
        self.assertEqual(h.open_sets[2][31], 3)
        self.assertEqual(h.claimed_tile[2], 31)
        self.assertEqual(h.claimed_player[2], 3)

    def test_kakan(self):
        h = hand.Hand(0)
        h.open_sets[0][1] = 3
        h.kakan(1)
        self.assertEqual(h.open_sets[0][1], 4)

    def test_ankan(self):
        h = hand.Hand(0)
        h.main_hand = [0,0,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,0,1,0,0,0,
                       0,0,2,0,0,0,0,0,0,0,
                       0,3,1,0,1,0,0]
        h.ankan(31)
        self.assertEqual(h.main_hand[31],0)
        self.assertEqual(h.open_sets[0][31], 3)
        self.assertEqual(h.claimed_tile[0], 31)
        self.assertEqual(h.claimed_player[0], 0)


    def test_add(self):
        h = hand.Hand(0)
        h.add(1)
        self.assertEqual(h.main_hand[1], 1)
        h.add(1)
        self.assertEqual(h.main_hand[1], 2)

    def test_discard(self):
        h = hand.Hand(0)
        h.main_hand[1] = 2
        h.discard(1)
        self.assertEqual(h.main_hand[1], 1)
        h.discard(1)
        self.assertEqual(h.main_hand[1], 0)

    def test_is_open(self):
        h = hand.Hand(0)
        h.claimed_player.append(0)
        h.claimed_player.append(0)
        self.assertIs(h.is_open(), False)
        h.claimed_player.append(1)
        self.assertIs(h.is_open(), True)

    def test_open_num(self):
        h = hand.Hand(0)
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,0,2,2,0,1,0,0,0,0,
                       0,0,2,1,0,1,0,0,0,0,
                       0,0,2,1,0,1,0]
        self.assertEqual(h.open_num(), 0)
        h.claim([12,12],12,1)
        h.main_hand[15] -= 1
        self.assertEqual(h.open_num(), 1)

    def test_calc_shanten_seven(self):
        h = hand.Hand(0)
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,0,2,2,0,1,0,0,0,0,
                       0,0,2,1,0,1,0,0,0,0,
                       0,0,2,1,0,1,0]
        self.assertEqual(hand.calc_shanten_seven(h), 2)
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,0,2,2,0,0,0,0,0,0,
                       0,0,2,2,0,0,0,0,0,0,
                       0,0,2,2,2,0,0]
        self.assertEqual(hand.calc_shanten_seven(h), -1)

    def test_calc_shanten_kokushi(self):
        h = hand.Hand(0)
        h.main_hand = [0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       1,1,2,3,0,0,0]
        self.assertEqual(hand.calc_shanten_kokushi(h), 2)
        h.main_hand = [0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       1,1,1,1,1,1,2]
        self.assertEqual(hand.calc_shanten_kokushi(h), -1)


    def test_calc_shanten_normal(self):
        h = hand.Hand(0)
        h.main_hand = [0,1,1,1,0,0,0,0,2,2,
                       0,0,0,0,1,1,1,0,0,0,
                       0,0,0,0,0,0,0,1,1,1,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten_normal(h), 0)
        h.main_hand = [0,1,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,1,1,0,0,0,
                       0,0,1,0,1,0,0,1,1,1,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten_normal(h), 1)
        h.main_hand = [0,1,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,1,1,0,0,0,
                       0,0,0,0,0,0,0,1,1,1,
                       0,0,2,0,0,0,0]
        self.assertEqual(hand.calc_shanten_normal(h), 0)
        h.main_hand = [0,1,1,0,1,1,0,0,0,0,
                       0,0,0,0,0,1,1,1,0,0,
                       0,1,1,1,0,1,1,0,1,1,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten_normal(h), 2)
        h.main_hand = [0,1,1,0,1,1,0,0,0,0,
                       0,0,0,0,0,1,1,1,0,0,
                       0,1,1,1,0,1,1,0,2,0,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten_normal(h), 1)
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,1,1,1,0,0,0,0,0,0,
                       0,0,0,1,3,1,1,1,0,0,
                       0,0,0,1,0,2,0]
        self.assertEqual(hand.calc_shanten_normal(h), 1)
        h.main_hand = [0,3,1,1,1,1,1,1,1,3,
                       0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten_normal(h), 0)

    def test_calc_shanten(self):
        h = hand.Hand(0)
        # seven_pair
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,0,2,2,0,1,0,0,0,0,
                       0,0,2,1,0,1,0,0,0,0,
                       0,0,2,1,0,1,0]
        self.assertEqual(hand.calc_shanten(h), 2)
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,0,2,2,0,0,0,0,0,0,
                       0,0,2,2,0,0,0,0,0,0,
                       0,0,2,2,2,0,0]
        self.assertEqual(hand.calc_shanten(h), -1)
        # kokushi
        h.main_hand = [0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       1,1,2,3,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 2)
        h.main_hand = [0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       0,1,0,0,0,0,0,0,0,1,
                       1,1,1,1,1,1,2]
        self.assertEqual(hand.calc_shanten(h), -1)
        # normal
        h.main_hand = [0,1,1,1,0,0,0,0,2,2,
                       0,0,0,0,1,1,1,0,0,0,
                       0,0,0,0,0,0,0,1,1,1,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 0)
        h.main_hand = [0,1,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,1,1,0,0,0,
                       0,0,1,0,1,0,0,1,1,1,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 1)
        h.main_hand = [0,1,1,1,0,0,0,1,1,0,
                       0,0,0,0,1,1,1,0,0,0,
                       0,0,0,0,0,0,0,1,1,1,
                       0,0,2,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 0)
        h.main_hand = [0,1,1,0,1,1,0,0,0,0,
                       0,0,0,0,0,1,1,1,0,0,
                       0,1,1,1,0,1,1,0,1,1,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 2)
        h.main_hand = [0,1,1,0,1,1,0,0,0,0,
                       0,0,0,0,0,1,1,1,0,0,
                       0,1,1,1,0,1,1,0,2,0,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 1)
        h.main_hand = [0,0,0,0,0,0,0,0,0,0,
                       0,1,1,1,0,0,0,0,0,0,
                       0,0,0,1,3,1,1,1,0,0,
                       0,0,0,1,0,2,0]
        self.assertEqual(hand.calc_shanten(h), 1)
        h.main_hand = [0,3,1,1,1,1,1,1,1,3,
                       0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0,0,0,0,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 0)
        h.main_hand = [0,3,0,0,3,0,3,0,0,0,
                       0,0,0,0,0,0,3,0,0,0,
                       0,0,0,1,0,0,0,0,0,0,
                       0,0,0,0,0,0,0]
        self.assertEqual(hand.calc_shanten(h), 0)
        # pong
        h2 = hand.Hand(0)
        h2.main_hand = [0,3,0,0,3,0,3,0,0,0,
                       0,0,0,0,0,0,2,0,0,0,
                       0,0,0,1,0,0,0,0,0,0,
                       0,0,0,0,0,0,0]
        h2.claim([16,16], 16, 1)
        self.assertEqual(hand.calc_shanten(h2), 0)
        # daiminkan
        h2.claim([1,1,1], 1, 2)
        self.assertEqual(hand.calc_shanten(h2), 0)
        # chow
        h2 = hand.Hand(0)
        h2.main_hand = [0,3,0,0,3,0,3,0,0,0,
                       0,0,0,0,0,0,1,0,0,0,
                       0,0,0,1,1,0,0,0,0,0,
                       0,0,0,0,0,0,0]
        h2.claim([23,24], 25, 1)
        self.assertEqual(hand.calc_shanten(h2), 0)
        h2.main_hand[16] = 2
        self.assertEqual(hand.calc_shanten(h2), -1)


if __name__ == '__main__':
    unittest.main()
