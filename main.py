import chess
import chess.engine
from board import *
from graph import *


def run():
    engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\nadal\Downloads\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe')

    board = chess.Board()
    player = False
    move_engine = "a0a0"
    move_player = "a0a0"

    while not board.is_game_over():
        if not player:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            #call arduino
            print(get_path(move_engine[2:] + result.move))
            #call arduino
            print(get_path(result.move))
            move_engine = result.move
            print("Computer has played : " + str(result.move))
            with open("board.txt", "w") as f:
                f.write(str(board))
            player = True
        else:
            input("Press enter when you have played!")
            with open("board.txt", "r") as f:
                played_board = "".join(f.readlines())
            move_player = diff(board, played_board)
            result_move = chess.Move.from_uci(str(move_player))
            board.push(result_move)
            print("You have played : " + str(result_move))
            player = False
    
    engine.quit()

if __name__ == "__main__":
    run()