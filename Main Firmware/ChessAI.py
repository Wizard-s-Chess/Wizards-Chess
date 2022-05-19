import chess
import chess.engine

class ChessAI:

    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(r'stockfish_15_x64_avx2.exe')
        self.board = chess.Board()
    #Plays automatically a move on the board, and returns the move that was made
    def play_move_auto(self):
        res = self.engine.play(board, chess.engine.Limit(time=0.1))
        move = res.move
        self.board.push(move)
        return move
    #Plays a move given as a parameter, returns true if the move is performed(legal) and false if not
    def play_move(self,move):
        #Add return rating of the move, instead of legal or not
        if(self.is_move_legal(move)):
            res = chess.Move.from_uci(move)
            self.board.push(res)
            return True
        return False
    def commit_move(self,move):
        
    def destroy(self):
        self.engine.quit()
        
    def is_move_legal(self,difference):
        move = self.chess.Move.from_uci(difference)
        return move in self.board.legal_moves 

    def is_checkmate(self):

        return self.board.is_checkmate()

    #Checks if the current position is a checkmate.

    def is_stalemate(self):

        return self.board.is_stalemate()

    #Checks if the current position is a stalemate.

    def is_insufficient_material(self):

        return self.board.is_insufficient_material()

    #Checks if neither side has sufficient winning material 

    def capture_en_passant(self, from_square, to_square):
        
        return self.board.is_en_passant(self.chess.Move(from_square=from_square, to_square=to_square))

    #Checks if the given pseudo-legal move is an en passant capture.

    def is_capture(self, from_sqaure, to_square):

        return self.board.is_capture(self.chess.Move(from_square=from_sqaure, to_square=to_square))

    #Checks if the given pseudo-legal move is a capture.
    def is_game_over():
        return self.board.is_game_over()
    def reset(self):
        return self.board.reset_board()
    def get_board(self):
        return self.board