class Mahjong:
    def __init__(self, tiles):
        self.tiles = tiles
    
    # 1. Mahjong has exactly four players.
    def has_4_players(self):
        return len(self.tiles) == 4