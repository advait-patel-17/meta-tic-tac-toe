from game.board import Board, BoardWinState
from enum import Enum

class MetaWinState(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2
    TIED = 3
    UNDECIDED = 4


class MetaBoard:
    def __init__(self) -> None:
        self.boards = [[Board() for j in range(3)] for i in range(3)]
        self.win_state = MetaWinState.UNDECIDED
    
    def __str__(self) -> str:
        result = ""
        rows = [[str(self.boards[i][j]).split("\n") for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(len(rows[i][0])):
                result += rows[i][0][j] + ("\t" * 2) + rows[i][1][j] + ("\t" * 2) + rows[i][2][j]
                result += "\n"
            result += "\n" * 3

        return result