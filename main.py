from numpy import tile
from game.board import Board
from game.tile import Tile
from game.metagame import MetaBoard
from game.state import State

def main():
    welcome_message = """Welcome to Tic Tac Toe Squared! The rules of the game are simple.
    There are 9 Tic-Tac-Toe boards arranged into 3 columns and 3 rows. Each turn, a player may make a single move in any one of the 9 game instances.
    Every time a player wins one of the game instances, they claim that corresponding tile in the meta-game. The game ends when a player wins the meta-game.

    Please note that the boards and tiles are numbered from 0 through 8.
    """
    print(welcome_message)
    g = MetaBoard()
    print("Here is what the board looks like: \n")
    print(g)
    current_player = State.PLAYER_1
    while (not g.is_won()):
        valid_params = False
        while (not valid_params):
            print("It is " + current_player.name + "'s turn.")
            inp1 = input("Please enter a valid board number. Valid board numbers are between 0 and 8 (inclusive) and may not refer to boards that have already been won: ")
            print("\n" + "-----------------" + "\n")
            inp2 = input("Please enter a valid tile number. Valid tile numbers are between 0 and 8 (inclusive) and may not refer to tiles that have already been played: ")
            valid_params = check_valid_board(inp1, inp2, g)
            if (valid_params):
                board_num = int(inp1)
                tile_num = int(inp2)
                g.play_turn(current_player, board_num=board_num, tile_num=tile_num)
                g.update_win_state()
                current_player = switch_turn(current_player)
        print(g)
    print("Congratulations! " + g.get_win_state().name + " has won the game!")


def switch_turn(player: State) -> State:
    if (player == State.PLAYER_1):
        return State.PLAYER_2
    
    return State.PLAYER_1

def check_valid_board(inp1: str, inp2: str, game: MetaBoard) -> bool:
    if (not inp1.isdigit() or not inp2.isdigit()):
        print("Please enter valid digits.")
        return False
    board_num = int(inp1)
    tile_num = int(inp2)
    if (0 <= board_num <= 8 and board_num not in game.get_unplayable_boards()):
        board = game.boards[board_num // 3][board_num % 3]
        if (isinstance(tile_num, int) and 0 <= tile_num <= 8 and tile_num not in board.get_unplayable_tiles()):
            return True
        else:
            print("Please input a valid tile number.")
            return False
    else:
        print("Please enter a valid board number.")
        return False


main()
