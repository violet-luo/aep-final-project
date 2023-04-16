import unittest
from src.mahjong import Mahjong 

class TestMahjong(unittest.TestCase):
    # 1. Test if Mahjong has exactly four players
    def test_four_players_should_return_true(self):
        mahjong = Mahjong([[],[],[],[]])
        self.assertTrue(mahjong.has_4_players())

    def test_three_players_should_return_false(self):
        mahjong = Mahjong([[],[],[]])
        self.assertFalse(mahjong.has_4_players())

    # 2. Test if each player has 14 tiles.
    def test_each_player_has_14_tiles_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*14])
        self.assertTrue(mahjong.each_player_has_14_tiles())

    def test_each_player_has_13_tiles_should_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*13])
        self.assertFalse(mahjong.each_player_has_14_tiles())

    # 3. Test if each tile is numeric.
    def test_numeric_tiles_shuold_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*14])
        self.assertTrue(mahjong.each_tile_is_numeric())
    
    def test_numeric_tiles_in_int_and_str_shuold_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*13 + ['4']])
        self.assertTrue(mahjong.each_tile_is_numeric())

    def test_alphanumeric_tiles_shuold_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*13 + ['a']])
        self.assertFalse(mahjong.each_tile_is_numeric())

if __name__ == '__main__':
    unittest.main()