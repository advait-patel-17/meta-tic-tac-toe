from game.board import Board
from game.state import State


class MetaBoard:
    def __init__(self) -> None:
        self.boards = [[Board() for j in range(3)] for i in range(3)]
        self.__win_state = State.UNDECIDED
        self.__unplayable_board_nums = set()


    def play_turn(self, player: State, board_num: int, tile_num: int):
        if (board_num not in self.__unplayable_board_nums and 0 <= board_num <= 8):
            q = board_num // 3
            r = board_num % 3
            board = self.boards[q][r]
            board.play_turn(player, tile_num)
            self.update_win_state()
            
            self.update_unplayable_boards()
    
    def get_win_state(self) -> State:
        return self.__win_state

    def is_won(self) -> bool:
        return self.__win_state != State.UNDECIDED
    
    def update_unplayable_boards(self):
        for row in range(3):
            for col in range(3):
                if (not self.boards[row][col].is_playable_board()):
                    self.__unplayable_board_nums.add(row * 3 + col)

    def update_win_state(self):
        for row in range(3):
            if (self.boards[row][0].get_win_state() == self.boards[row][1].get_win_state() == self.boards[row][2].get_win_state() == State.PLAYER_1):
                self.__win_state = State.PLAYER_1
                return
            if (self.boards[row][0].get_win_state() == self.boards[row][1].get_win_state() == self.boards[row][2].get_win_state() == State.PLAYER_2):
                self.__win_state = State.PLAYER_2
                return

            if (self.boards[0][row].get_win_state() == self.boards[1][row].get_win_state() == self.boards[2][row].get_win_state() == State.PLAYER_1):
                self.__win_state = State.PLAYER_1
                return
            
            if (self.boards[0][row].get_win_state() == self.boards[1][row].get_win_state() == self.boards[2][row].get_win_state() == State.PLAYER_2):
                self.__win_state = State.PLAYER_2
                return

        #check diagnonals
        if (self.boards[0][0].get_win_state() == self.boards[1][1].get_win_state() == self.boards[2][2].get_win_state() == State.PLAYER_1):
            self.__win_state = State.PLAYER_1
            return
        
        if (self.boards[0][2].get_win_state() == self.boards[1][1].get_win_state() == self.boards[2][0].get_win_state() == State.PLAYER_2):
            self.__win_state = State.PLAYER_2
            return
        

        
    
    def __str__(self) -> str:
        result = ""
        rows = [[str(self.boards[i][j]).split("\n") for j in range(3)] for i in range(3)]

        rownum = 0
        for i in range(3):
            result += "Board #" + str(rownum) + ": " + self.boards[rownum // 3][rownum % 3].get_win_state().name
            result += "\t" * 2
            result += "Board #" + str(rownum + 1) + ": " + self.boards[rownum // 3][(rownum % 3) + 1].get_win_state().name
            result += "\t" * 2
            result += "Board #" + str(rownum + 2) + ": " + self.boards[rownum // 3][(rownum % 3) + 2].get_win_state().name
            result += "\n" 
            for j in range(len(rows[i][0])):
                result += rows[i][0][j] + ("\t" * 2) + rows[i][1][j] + ("\t" * 2) + rows[i][2][j]
                result += "\n"
            result += "\n" * 3
            rownum += 3

        return result

    def get_unplayable_boards(self):
        return self.__unplayable_board_nums


    