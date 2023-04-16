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

    # 4. Test if each tile is integer.
    def test_integer_tiles_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*14])
        self.assertTrue(mahjong.each_tile_is_integer())
    
    def test_decimal_tiles_should_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*13 + [4.0]])
        self.assertFalse(mahjong.each_tile_is_integer())

    # 5. Test each tile is between 1 and 9.
    def test_tiles_between_1_and_9_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*14])
        self.assertTrue(mahjong.each_tile_is_between_1_and_9())
    
    def test_tiles_with_0_should_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*13 + [0]])
        self.assertFalse(mahjong.each_tile_is_between_1_and_9())

    def test_tiles_with_10_should_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [4]*13 + [10]])
        self.assertFalse(mahjong.each_tile_is_between_1_and_9())

    # 6. Test if one pair and four combinations is a winning hand.
    def test_one_pair_four_combinations_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,2,2,3,3,3,4,4,4,5,5,5]])
        self.assertTrue(mahjong.one_pair_and_four_combinations_is_winning_hand())
    
    def test_one_pair_three_combinations_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,2,2,3,3,3,4,4,4]])
        self.assertFalse(mahjong.one_pair_and_four_combinations_is_winning_hand())

if __name__ == '__main__':
    unittest.main()