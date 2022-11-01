from game.state import State

class Tile:
    def __init__(self, state: State) -> None:
        self.state = state
    
    def played(self) -> bool:
        return self.state == State.PLAYER_1 or self.state == State.PLAYER_2

    def __eq__(self, other) -> bool:
        return self.state == other.state
    
    def __str__(self) -> str:
        if (self.state == State.PLAYER_1):
            return "O"
        if (self.state == State.PLAYER_2):
            return "X"
        return "-"