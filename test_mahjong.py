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
    
    def test_one_pair_three_combinations_is_winning_hand_should_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,2,2,3,3,3,4,4,4]])
        self.assertFalse(mahjong.one_pair_and_four_combinations_is_winning_hand())

    # 7. Test if one pair and four consecutives is a winning hand.
    def test_one_pair_four_consecutives_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,3,4,5,6,7,2,3,4,5,6,7]])
        self.assertTrue(mahjong.one_pair_and_four_consecutives_is_winning_hand())
    
    def test_one_pair_four_consecutives_is_winning_hand_should_return_true_2(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,1,2,3,1,2,3,7,8,9,7,8,9]])
        self.assertTrue(mahjong.one_pair_and_four_consecutives_is_winning_hand())
    
    def test_one_pair_three_consecutives_is_winning_hand_should_return_false(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,1,2,3,1,2,3,7,8,9,7,8,8]])
        self.assertFalse(mahjong.one_pair_and_four_consecutives_is_winning_hand())

    # 8. Test if one pair and four combinations/consecutives is a winning hand.
    def test_one_pair_one_combinations_three_consecutives_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,2,2,3,3,3,4,4,4,5,6,7]])
        self.assertTrue(mahjong.one_pair_and_four_combinations_consecutives_is_winning_hand())
    
    def test_one_pair_two_combinations_two_consecutives_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,2,2,3,3,3,4,5,6,7,8,9]])
        self.assertTrue(mahjong.one_pair_and_four_combinations_consecutives_is_winning_hand())

    def test_one_pair_three_combinations_one_consecutives_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([[1]*14, [2]*14, [3]*14, [1,1,2,2,2,3,3,3,4,4,4,5,6,7]])
        self.assertTrue(mahjong.one_pair_and_four_combinations_consecutives_is_winning_hand())

    # 9. Test if seven pairs is a winning hand.
    def test_seven_pairs_is_winning_hand_should_return_true(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,7],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,7], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,7], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,7]])
        self.assertTrue(mahjong.seven_pairs_is_a_winning_hand())

    def test_six_pairs_is_winning_hand_should_return_false(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8]])
        self.assertFalse(mahjong.seven_pairs_is_a_winning_hand())

    # 10. Test if winning hand priority is correct. 
    def test_seven_pairs_compared_with_four_combinations_should_return_seven_pairs(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,7], # seven pairs
            [1,1,2,2,2,3,3,3,4,4,4,5,5,5]]) # one pair and four combinations
        self.assertEqual('Seven pairs.', mahjong.get_winning_hand_type())

    def test_four_combinations_compared_with_combinations_and_consecutives_should_return_four_combinations(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,2,3,3,3,4,4,4,5,5,5], # one pair and four combinations
            [1,1,2,2,2,3,3,3,4,5,6,7,8,9]]) # one pair and combinations and consecutives
        self.assertEqual('Four combinations or four consecutives.', mahjong.get_winning_hand_type())

    def test_four_consecutives_compared_with_combinations_and_consecutives_should_return_four_consecutives(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,1,2,3,2,3,4,3,4,5,4,5,6], # one pair and four consecutives
            [1,1,2,2,2,3,3,3,4,5,6,7,8,9]]) # one pair and combinations and consecutives
        self.assertEqual('Four combinations or four consecutives.', mahjong.get_winning_hand_type())
    
    def test_four_combinations_and_consecutives_should_return_four_combinations_and_consecutives(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,2,3,3,3,4,5,6,7,8,9]]) # one pair and combinations and consecutives
        self.assertEqual('Four combinations/consecutives.', mahjong.get_winning_hand_type())
    
    def test_no_winning_hand_should_return_no_winning_hand(self):
        mahjong = Mahjong([
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8],
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8], 
            [1,1,2,2,3,3,4,4,5,5,6,6,7,8]])
        self.assertEqual('No winning hand.', mahjong.get_winning_hand_type()) 

if __name__ == '__main__':
    unittest.main()