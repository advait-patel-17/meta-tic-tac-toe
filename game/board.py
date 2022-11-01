from game.tile import Tile
from game.state import State

class Board:
    def __init__(self) -> None:
        self._tiles = [[Tile(State.UNDECIDED) for i in range(3)] for j in range(3)]
        self._win_state = State.UNDECIDED
        self._turns = 0
        self._unplayable_tiles = set()

    def is_playable_board(self) -> bool:
        self.update_win_state()
        return self._win_state == State.UNDECIDED

    def get_win_state(self) -> State:  
        return self._win_state
    
    def play_turn(self, player: State, tile_num: int):
        if (tile_num not in self._unplayable_tiles):
            q = tile_num // 3
            r = tile_num % 3
            tile = self._tiles[q][r]
            if (not tile.played()):
                tile.state = player
            self._turns += 1
            self._unplayable_tiles.add(tile_num)
            self.update_win_state()

    def get_unplayable_tiles(self) -> set():
        return self._unplayable_tiles

    def update_win_state(self):
        player_1_win = [Tile(State.PLAYER_1) for i in range(3)]
        player_2_win = [Tile(State.PLAYER_2) for i in range(3)]

        #check rows
        for row in self._tiles:
            if (row == player_1_win):
                self._win_state = State.PLAYER_1
                return
            if (row == player_2_win):
                self._win_state = State.PLAYER_2
                return
        
        flipped = [[self._tiles[col][row] for col in range(len(self._tiles[row]))] for row in range(len(self._tiles))]

        #check cols
        for col in flipped:
            if (col == player_1_win):
                self._win_state = State.PLAYER_1
                return
            if (col == player_2_win):
                self._win_state = State.PLAYER_2
                return

        #check diagonals
        if (self._tiles[0][0] == self._tiles[1][1] == self._tiles[2][2] == player_1_win[0]):
            self._win_state = State.PLAYER_1
            return
        
        if (self._tiles[0][0] == self._tiles[1][1] == self._tiles[2][2] == player_2_win[0]):
            self._win_state = State.PLAYER_2
            return
            
        if (self._tiles[0][2] == self._tiles[1][1] == self._tiles[2][0] == player_1_win[0]):
            self._win_state = State.PLAYER_1
            return

        if (self._tiles[0][2] == self._tiles[1][1] == self._tiles[2][0] == player_2_win[0]):
            self._win_state = State.PLAYER_2
            return

        # check to see if all tiles have been played. if they have and the function got to this point,
        # the board is tied
        if (self._turns == 9):
            self.reset()
            return
        
        self._win_state = State.UNDECIDED
        

    
    def __str__(self) -> str:
        bars = "     |     |     "
        dash = "-----------------"
        row1 = "  "+ str(self._tiles[0][0]) + "  |  " + str(self._tiles[0][1]) + "  |  " + str(self._tiles[0][2]) + "  "
        row2 = "  "+ str(self._tiles[1][0]) + "  |  " + str(self._tiles[1][1]) + "  |  " + str(self._tiles[1][2]) + "  "
        row3 = "  "+ str(self._tiles[2][0]) + "  |  " + str(self._tiles[2][1]) + "  |  " + str(self._tiles[2][2]) + "  "
        result = bars + "\n" + row1 + "\n" + bars + "\n" + dash + "\n" + bars + "\n" + row2 + "\n" + bars + "\n" + dash + "\n" + bars + "\n" + row3 + "\n" + bars
        return result

    def reset(self):
        for row in self._tiles:
            for tile in row:
                tile.state = State.UNUSED
        self._win_state = State.UNDECIDED
        self._turns = 0
        self._unplayable_tiles = set()
