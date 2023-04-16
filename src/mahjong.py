from collections import Counter

class Mahjong:
    def __init__(self, tiles):
        self.tiles = tiles
    
    # 1. Mahjong has exactly four players.
    def has_4_players(self):
        return len(self.tiles) == 4
    
    # 2. Each player has 14 tiles.
    def each_player_has_14_tiles(self):
        for tile in self.tiles:
            if len(tile) != 14:
                return False
        return True
    
    # 3. Each tile is numeric.
    def each_tile_is_numeric(self):
        for tile in self.tiles:
            for t in tile:
                t_str = str(t)
                if not t_str.isnumeric():
                    return False
        return True
    
    # 4. Each tile is integer.
    def each_tile_is_integer(self):
        for tile in self.tiles:
            for t in tile:
                if not isinstance(t, int):
                    return False
        return True

    # 5. Each tile is between 1 and 9.
    def each_tile_is_between_1_and_9(self):
        for tile in self.tiles:
            for t in tile:
                if t not in range(1, 10):
                    return False
        return True
    
    # 6. A winning hand can have one pair and four combinations.
    def one_pair_and_four_combinations_is_winning_hand(self):
        for tile in self.tiles:
            counter = Counter(tile)
            
            num_pairs, num_combinations = 0, 0
            for cnt in counter.values():
                if cnt == 2:
                    num_pairs += 1
                elif cnt == 3:
                    num_combinations += 1
            
            if num_pairs == 1 and num_combinations == 4:
                return True

        return False
    