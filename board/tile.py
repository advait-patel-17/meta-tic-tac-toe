from enum import Enum

class TileState(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2
    UNUSED = 3

class Tile:
    def __init__(self, state: TileState) -> None:
        self._state = state
    
    def played(self) -> bool:
        return self._state == TileState.PLAYER_1 or self.state == TileState.PLAYER_2

    def get_state(self) -> TileState:
        return self._state