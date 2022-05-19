import chess
import chess.engine
from arduino import *
from board import *
from capture import *
from computervision import *
from graph import *
from choose_options import *


def launch_game(ser):
    engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\nadal\Downloads\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe')

    board = chess.Board()
    player = False
    move_engine = "a1a1"
    move_player = "a1a1"

    options = [["Choose level : ", "Level " + str(i + 1)] for i in range(10)]
    choose_between(options)

    while not board.is_game_over():
        if not player:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            path = get_path(move_engine[2:] + str(result.move))
            move_motors(ser, path, active_magnet=True)
            path = get_path(str(result.move))
            print("engine played : " + str(result.move))
            move_motors(ser, path, active_magnet=False)
            move_engine = str(result.move)
            player = True
        else:
            display("You turn : press", "OK to confirm!")
            while not button_pressed()[1]:
                pass
            display("Wait please ...", "Engine playing")
            played_board = get_move_from_player()
            print(convert_board(board))
            move_player = diff(board, played_board)
            print(move_player)
            result_move = chess.Move.from_uci(str(move_player))
            print("you played : " + str(result_move))
            board.push(result_move)
            player = False
    
    engine.quit()