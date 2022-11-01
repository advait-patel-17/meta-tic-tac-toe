from enum import Enum

class TileState(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2
    UNUSED = 3

class Tile:
    def __init__(self, state: TileState) -> None:
        self.state = state
    
    def played(self) -> bool:
        return self.state == TileState.PLAYER_1 or self.state == TileState.PLAYER_2

    def __eq__(self, other) -> bool:
        return self.state == other.state
    
    def __str__(self) -> str:
        if (self.state == TileState.PLAYER_1):
            return "O"
        if (self.state == TileState.PLAYER_2):
            return "X"
        return "-"