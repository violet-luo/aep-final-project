from collections import Counter

class Mahjong:
    """
    This is a class that determines whether the mahjong tiles are valid and which player wins.
    """
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
    
    # 7. A winning hand can have one pair and four consecutives.
    def one_pair_and_four_consecutives_is_winning_hand(self):
        for tile in self.tiles:
            counts = [0] * 10
            for t in tile:
                counts[t] += 1

            def backtrack():
                if sum(counts) == 0: # exit condition
                    return True
                
                for i in range(8): # find consecutives
                    if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
                        counts[i] -= 1
                        counts[i+1] -= 1
                        counts[i+2] -= 1
                        if backtrack():
                            return True
                        counts[i] += 1
                        counts[i+1] += 1
                        counts[i+2] += 1

                return False
            
            for i in range(10): # find pair
                if counts[i] >= 2:
                    counts[i] -= 2
                    if backtrack():
                        return True
                    counts[i] += 2
                    
        return False

    # 8. A winning hand can have one pair and four combinations/consecutives.
    def one_pair_and_four_combinations_consecutives_is_winning_hand(self):
        for tile in self.tiles:
            counts = [0] * 10
            for t in tile:
                counts[t] += 1

            def backtrack():
                if sum(counts) == 0: # exit condition
                    return True
                
                for i in range(8): # find consecutives
                    if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
                        counts[i] -= 1
                        counts[i+1] -= 1
                        counts[i+2] -= 1
                        if backtrack():
                            return True
                        counts[i] += 1
                        counts[i+1] += 1
                        counts[i+2] += 1
                        
                for i in range(10): # find combinations
                    if counts[i] >= 3:
                        counts[i] -= 3
                        if backtrack():
                            return True
                        counts[i] += 3

                return False
            
            for i in range(10): # find pair
                if counts[i] >= 2:
                    counts[i] -= 2
                    if backtrack():
                        return True
                    counts[i] += 2
                    
        return False
    
    # 9. A winning hand can have seven pairs.
    def seven_pairs_is_a_winning_hand(self):
        for tile in self.tiles:
            pairs = 0
            for i in range(1, 10):
                if tile.count(i) == 2:
                    pairs += 1
            if pairs == 7:
                return True
        return False
    
    # 10. If multiple winning hands, seven pairs > 4 combinations = 4 consecutives > 4 combinations/consecutives
    def get_winning_hand_type(self):
        if self.seven_pairs_is_a_winning_hand():
            return 'Seven pairs.'
        elif self.one_pair_and_four_combinations_is_winning_hand() or self.one_pair_and_four_consecutives_is_winning_hand():
            return 'Four combinations or four consecutives.'
        elif self.one_pair_and_four_combinations_consecutives_is_winning_hand():
            return 'Four combinations/consecutives.'
        return 'No winning hand.'
