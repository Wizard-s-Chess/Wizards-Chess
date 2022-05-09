import chess
import chess.engine
from arduino import *
from board import *
from capture import *
from computervision import *
from graph import *


def run():
    engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\nadal\Downloads\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe')

    board = chess.Board()
    player = False
    move_engine = "a1a1"
    move_player = "a1a1"

    while not board.is_game_over():
        if not player:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            path = get_path(move_engine[2:] + str(result.move))
            move_motors(path)
            # TODO: activate magnet
            path = get_path(str(result.move))
            move_motors(path)
            # TODO: deactivate magnet
            move_engine = str(result.move)
            print("Computer has played : " + str(result.move))
            player = True
        else:
            input("Press enter when you have played!")
            capture()
            played_board = get_move_from_player()
            print(played_board)
            move_player = diff(board, played_board)
            result_move = chess.Move.from_uci(str(move_player))
            board.push(result_move)
            print("You have played : " + str(result_move))
            player = False
    
    engine.quit()

if __name__ == "__main__":
    run()