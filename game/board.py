from game.tile import Tile
from game.state import State

class Board:
    def __init__(self) -> None:
        self.__tiles = [[Tile(State.UNDECIDED) for i in range(3)] for j in range(3)]
        self.__win_state = State.UNDECIDED
        self.__turns = 0
        self.__unplayable_tiles = set()

    def is_playable_board(self) -> bool:
        self.update_win_state()
        return self.__win_state == State.UNDECIDED

    def get_win_state(self) -> State:  
        return self.__win_state
    
    def play_turn(self, player: State, tile_num: int):
        if (tile_num not in self.__unplayable_tiles):
            q = tile_num // 3
            r = tile_num % 3
            tile = self.__tiles[q][r]
            if (not tile.played()):
                tile.state = player
            self.__turns += 1
            self.__unplayable_tiles.add(tile_num)
            self.update_win_state()

    def get_unplayable_tiles(self) -> set():
        return self.__unplayable_tiles

    def update_win_state(self):
        player_1_win = [Tile(State.PLAYER_1) for i in range(3)]
        player_2_win = [Tile(State.PLAYER_2) for i in range(3)]

        #check rows
        for row in self.__tiles:
            if (row == player_1_win):
                self.__win_state = State.PLAYER_1
                return
            if (row == player_2_win):
                self.__win_state = State.PLAYER_2
                return
        
        flipped = [[self.__tiles[col][row] for col in range(len(self.__tiles[row]))] for row in range(len(self.__tiles))]

        #check cols
        for col in flipped:
            if (col == player_1_win):
                self.__win_state = State.PLAYER_1
                return
            if (col == player_2_win):
                self.__win_state = State.PLAYER_2
                return

        #check diagonals
        if (self.__tiles[0][0] == self.__tiles[1][1] == self.__tiles[2][2] == player_1_win[0]):
            self.__win_state = State.PLAYER_1
            return
        
        if (self.__tiles[0][0] == self.__tiles[1][1] == self.__tiles[2][2] == player_2_win[0]):
            self.__win_state = State.PLAYER_2
            return
            
        if (self.__tiles[0][2] == self.__tiles[1][1] == self.__tiles[2][0] == player_1_win[0]):
            self.__win_state = State.PLAYER_1
            return

        if (self.__tiles[0][2] == self.__tiles[1][1] == self.__tiles[2][0] == player_2_win[0]):
            self.__win_state = State.PLAYER_2
            return

        # check to see if all tiles have been played. if they have and the function got to this point,
        # the board is tied
        if (self.__turns == 9):
            self.reset()
            return
        
        self.__win_state = State.UNDECIDED
        

    
    def __str__(self) -> str:
        bars = "     |     |     "
        dash = "-----------------"
        row1 = "  "+ str(self.__tiles[0][0]) + "  |  " + str(self.__tiles[0][1]) + "  |  " + str(self.__tiles[0][2]) + "  "
        row2 = "  "+ str(self.__tiles[1][0]) + "  |  " + str(self.__tiles[1][1]) + "  |  " + str(self.__tiles[1][2]) + "  "
        row3 = "  "+ str(self.__tiles[2][0]) + "  |  " + str(self.__tiles[2][1]) + "  |  " + str(self.__tiles[2][2]) + "  "
        result = bars + "\n" + row1 + "\n" + bars + "\n" + dash + "\n" + bars + "\n" + row2 + "\n" + bars + "\n" + dash + "\n" + bars + "\n" + row3 + "\n" + bars
        return result

    def reset(self):
        for row in self.__tiles:
            for tile in row:
                tile.state = State.UNDECIDED
        self.__win_state = State.UNDECIDED
        self.__turns = 0
        self.__unplayable_tiles = set()
