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