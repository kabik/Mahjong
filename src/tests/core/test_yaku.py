import unittest

from src.core import yaku
from src.core import hand

class TestYaku(unittest.TestCase):
    # 立直
    def test_is_reach(self):
        pass

    # 役牌
    def test_is_value_tiles(self):
        pass

    # 断么
    def test_is_all_simples(self):
        pass

    # 平和
    def test_is_all_runs(self):
        pass

    # 面前自摸
    def test_is_concealed_self_draw(self):
        pass

    # 一発
    def test_is_first_turn_win(self):
        pass

    # 一盃口
    def test_is_double_run(self):
        pass

    # 河底撈魚
    def test_is_final_tile_win_from_the_river(self):
        pass

    # 海底摸月
    def test_is_final_tile_win_from_the_wall(self):
        pass

    # 嶺上開花
    def test_is_kings_tile_draw(self):
        pass

    # 二重立直
    def test_is_double_reach(self):
        pass

    # 搶槓
    def test_is_add_a_quad(self):
        pass

    # 対々和
    def test_is_all_triples(self):
        pass

    # 三色同順
    def test_is_three_color_runs(self):
        pass

    # 七対子
    def test_is_seven_pairs(self):
        pass

    # 一気通貫
    def test_is_full_straight(self):
        pass

    # 混全帯
    def test_is_mixed_outside_hand(self):
        pass

    # 三暗刻
    def test_is_three_concealed_triples(self):
        pass

    # 小三元
    def test_is_little_dragons(self):
        pass

    # 混老頭
    def test_is_all_terminals_and_honors(self):
        pass

    # 三色同刻
    def test_is_three_color_triples(self):
        pass

    # 三槓子
    def test_is_three_quads(self):
        pass

    # 混一色
    def test_is_half_flush(self):
        pass

    # 清全帯
    def test_is_pure_outside_hand(self):
        pass

    # ニ盃口
    def test_is_two_double_runs(self):
        pass

    # 清一色
    def test_is_full_flush(self):
        pass

    # 四暗刻
    def test_is_four_concealed_triples(self):
        pass

    # 国士無双
    def test_is_thirteen_orphans(self):
        pass

    # 大三元
    def test_is_big_dragons(self):
        pass

    # 四喜和
    def test_is_four_winds(self):
        pass

    # 字一色
    def test_is_all_honors(self):
        pass

    # 清老頭
    def test_is_all_terminals(self):
        pass

    # 地和
    def test_is_blessing_of_earth(self):
        pass

    # 緑一色
    def test_is_all_green(self):
        pass

    # 九蓮宝燈
    def test_is_nine_gates(self):
        pass

    # 四槓子
    def test_is_four_quads(self):
        pass

    # 天和
    def test_is_blessing_of_heaven(self):
        pass


if __name__ == '__main__':
    unittest.main()
