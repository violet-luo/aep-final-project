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
