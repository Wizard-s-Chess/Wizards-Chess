import chess
import chess.engine

def convert_board(board):
    converted_board = str(board).replace("\n", "").replace(" ", "")
    pieces = "rqkbnrpPQKBNR"
    for char in pieces:
        converted_board = converted_board.replace(char,"X")
    return converted_board

def diff(previous_board, next_board):
    previous_string = convert_board(previous_board)
    next_string = convert_board(next_board)
    diff = [i for i in range(len(previous_string)) if previous_string[i] != next_string[i]]
    if previous_string[diff[0]] != 'X':
        diff = list(reversed(diff))
    initial_position = str(chr((diff[0]%8) + 97) + str(abs(diff[0]//8 - 8)))
    final_position = str(chr((diff[1]%8) + 97) + str(abs(diff[1]//8 - 8)))
    return initial_position + final_position

def convert_move():
    pass


def run():
    engine = chess.engine.SimpleEngine.popen_uci(r'C:\Users\nadal\Downloads\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe')

    board = chess.Board()
    player = False

    while not board.is_game_over():
        if not player:
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            print("Computer has played : " + str(result.move))
            with open("board.txt", "w") as f:
                f.write(str(board))
            player = True
        else:
            input("Press enter when you have played!")
            with open("board.txt", "r") as f:
                played_board = "".join(f.readlines())
            move = diff(board, played_board)
            result_move = chess.Move.from_uci(str(move))
            board.push(result_move)
            print("You have played : " + str(result_move))
            player = False
    
    engine.quit()

if __name__ == "__main__":
    run()