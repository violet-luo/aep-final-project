import unittest
from src.mahjong import Mahjong 

class TestMahjong(unittest.TestCase):
    # 1. Test if Mahjong has exactly four players
    def test_four_players_should_return_true(self):
        mahjong = Mahjong([[],[],[],[]])
        self.assertTrue(mahjong.has_4_players)

    def test_three_players_should_return_false(self):
        mahjong = Mahjong([[],[],[]])
        self.assertFalse(mahjong.has_4_players())

if __name__ == '__main__':
    unittest.main()