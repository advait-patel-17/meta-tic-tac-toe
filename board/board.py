from numpy import void
from board.tile import TileState
from tile import Tile
from enum import Enum

class WinState(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2
    TIED = 3
    UNDECIDED = 4

class Board:
    def __init__(self, num: int) -> None:
        self._num = num
        self._tiles = []
        for i in range(9):
            tile = Tile(TileState.UNUSED)
            self._tiles.append(tile)
        self._win_state = WinState.UNDECIDED

    def is_playable_board(self) -> bool:
        self.update_win_state()
        return self._win_state == WinState.UNDECIDED

    def get_num(self) -> int:
        return self._num

    def get_win_state(self) -> WinState:  
        return self._win_state
    
    def play_turn(self, player: TileState, tile_num: int):
        tile = self._tiles[tile_num]
        if (not tile.played()):
            tile.state = player

    def update_win_state(self):
        pass

    
    def print_board(self):
        pass
