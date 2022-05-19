import chess


def is_move_legal(difference, board):
    
    move = chess.Move.from_uci(difference)
    if move in board.legal_moves:
        return True
    else:
        return False

def is_checkmate(board):

    return board.is_checkmate()

#Checks if the current position is a checkmate.

def stalemate_check(board):

    return board.is_stalemate()

#Checks if the current position is a stalemate.

def has_insufficient_material(board):

    return board.is_insufficient_material()

#Checks if neither side has sufficient winning material 


def capture_en_passant(board, from_square, to_square):
    
    return board.is_en_passant(chess.Move(from_square=from_square, to_square=to_square))

#Checks if the given pseudo-legal move is an en passant capture.

def is_capture(board, from_sqaure, to_square):

    return board.is_capture(chess.Move(from_square=from_sqaure, to_square=to_square))

#Checks if the given pseudo-legal move is a capture.

def reset(board):
    
    return board.reset_board()






