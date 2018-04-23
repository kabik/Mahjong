import unittest

from src.core import tile

class TestTile(unittest.TestCase):
    manzu = (
                #(tile.Tile.M0, 0),
                (tile.Tile.M1, 1),
                (tile.Tile.M2, 2),
                (tile.Tile.M3, 3),
                (tile.Tile.M4, 4),
                (tile.Tile.M5, 5),
                (tile.Tile.M6, 6),
                (tile.Tile.M7, 7),
                (tile.Tile.M8, 8),
                (tile.Tile.M9, 9),
            )

    pinzu = (
                #(tile.Tile.P0, 10),
                (tile.Tile.P1, 11),
                (tile.Tile.P2, 12),
                (tile.Tile.P3, 13),
                (tile.Tile.P4, 14),
                (tile.Tile.P5, 15),
                (tile.Tile.P6, 16),
                (tile.Tile.P7, 17),
                (tile.Tile.P8, 18),
                (tile.Tile.P9, 19),
            )

    souzu = (
                #(tile.Tile.S0, 20),
                (tile.Tile.S1, 21),
                (tile.Tile.S2, 22),
                (tile.Tile.S3, 23),
                (tile.Tile.S4, 24),
                (tile.Tile.S5, 25),
                (tile.Tile.S6, 26),
                (tile.Tile.S7, 27),
                (tile.Tile.S8, 28),
                (tile.Tile.S9, 29),
            )

    winds = (
                (tile.Tile.TON, 30),
                (tile.Tile.NAN, 31),
                (tile.Tile.SHA, 32),
                (tile.Tile.PEI, 33),
            )

    dragons = (
                (tile.Tile.HAK, 34),
                (tile.Tile.HAT, 35),
                (tile.Tile.CHN, 36),
            )

    def test_define(self):
        for t, n in (self.manzu + self.pinzu + self.souzu + self.winds + self.dragons):
            self.assertEqual(t.value, n)

    def test_is_manzu(self):
        for t, n in self.manzu:
            self.assertIs(t.is_manzu(), True)
        for t, n in (self.pinzu + self.souzu + self.winds + self.dragons):
            self.assertIs(t.is_manzu(), False)

    def test_is_pinzu(self):
        for t, n in self.pinzu:
            self.assertIs(t.is_pinzu(), True)
        for t, n in (self.manzu + self.souzu + self.winds + self.dragons):
            self.assertIs(t.is_pinzu(), False)

    def test_is_souzu(self):
        for t, n in self.souzu:
            self.assertIs(t.is_souzu(), True)
        for t, n in (self.manzu + self.pinzu + self.winds + self.dragons):
            self.assertIs(t.is_souzu(), False)

    def test_is_wind(self):
        for t, n in self.winds:
            self.assertIs(t.is_wind(), True)
        for t, n in (self.manzu + self.pinzu + self.souzu + self.dragons):
            self.assertIs(t.is_wind(), False)

    def test_is_dragon(self):
        for t, n in self.dragons:
            self.assertIs(t.is_dragon(), True)
        for t, n in (self.manzu + self.pinzu + self.souzu + self.winds):
            self.assertIs(t.is_dragon(), False)

    def test_is_suit(self):
        for t, n in (self.manzu + self.pinzu + self.souzu):
            self.assertIs(t.is_suit(), True)
        for t, n in (self.winds + self.dragons):
            self.assertIs(t.is_suit(), False)

    def test_is_honor(self):
        for t, n in (self.winds + self.dragons):
            self.assertIs(t.is_honor(), True)
        for t, n in (self.manzu + self.pinzu + self.souzu):
            self.assertIs(t.is_honor(), False)

    def test_is_terminal(self):
        self.assertIs(tile.Tile.M1.is_terminal(), True)
        self.assertIs(tile.Tile.M2.is_terminal(), False)
        self.assertIs(tile.Tile.M8.is_terminal(), False)
        self.assertIs(tile.Tile.M9.is_terminal(), True)
        self.assertIs(tile.Tile.P1.is_terminal(), True)
        self.assertIs(tile.Tile.P2.is_terminal(), False)
        self.assertIs(tile.Tile.P8.is_terminal(), False)
        self.assertIs(tile.Tile.P9.is_terminal(), True)
        self.assertIs(tile.Tile.S1.is_terminal(), True)
        self.assertIs(tile.Tile.S2.is_terminal(), False)
        self.assertIs(tile.Tile.S8.is_terminal(), False)
        self.assertIs(tile.Tile.S9.is_terminal(), True)
        self.assertIs(tile.Tile.TON.is_terminal(), False)
        self.assertIs(tile.Tile.CHN.is_terminal(), False)

    def test_is_terminal_or_honor(self):
        self.assertIs(tile.Tile.M1.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.M2.is_terminal_or_honor(), False)
        self.assertIs(tile.Tile.M8.is_terminal_or_honor(), False)
        self.assertIs(tile.Tile.M9.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.P1.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.P2.is_terminal_or_honor(), False)
        self.assertIs(tile.Tile.P8.is_terminal_or_honor(), False)
        self.assertIs(tile.Tile.P9.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.S1.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.S2.is_terminal_or_honor(), False)
        self.assertIs(tile.Tile.S8.is_terminal_or_honor(), False)
        self.assertIs(tile.Tile.S9.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.TON.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.NAN.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.SHA.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.PEI.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.HAK.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.HAT.is_terminal_or_honor(), True)
        self.assertIs(tile.Tile.CHN.is_terminal_or_honor(), True)

    def test_dora_index_by_display_index(self):
        for i in range(0,3):
            for j in range(1,9):
                self.assertEqual(tile.dora_index_by_display_index(i*10+j), i*10+j+1)
            self.assertEqual(tile.dora_index_by_display_index(i*10+9), i*10+1)
        self.assertEqual(tile.dora_index_by_display_index(30), 31)
        self.assertEqual(tile.dora_index_by_display_index(31), 32)
        self.assertEqual(tile.dora_index_by_display_index(32), 33)
        self.assertEqual(tile.dora_index_by_display_index(33), 30)
        self.assertEqual(tile.dora_index_by_display_index(34), 35)
        self.assertEqual(tile.dora_index_by_display_index(35), 36)
        self.assertEqual(tile.dora_index_by_display_index(36), 34)

if __name__ == '__main__':
    unittest.main()
