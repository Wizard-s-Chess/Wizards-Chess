
import ChessboardGraph
import PhysicalBoard
import UserInteractor
import ComputerVision
import ChessAI
class WizardsChess:
    def __init__(self):
        print("initializing")
        self.chess_ai = chessAI()
        self.user_interactor = UserInteractor()
        self.physical_board = PhysicalBoard()
        self.is_game_finished = False
        
        
    def start(self):
        self.is_game_finished = False
        player_mode = self.user_interactor.get_game_mode()
        if player_mode:
            self.play_human_vs_ai()
        else:
            self.play_ai_vs_ai()

    def play_ai_vs_ai(self):
        ai_1_move = None
        ai_2_move = None
        is_ai_1_turn = True
        while not(self.is_game_finished):
            if(is_ai_1_turn):
                ai_1_move = self.chess_ai.play_move_auto()
                self.perform_move_on_board(str(move))
            else:
                ai_2_move = self.chess_ai.play_move_auto()
                self.perform_move_on_board(str(move))
            is_ai_1_turn = not is_ai_1_turn
        
            self.is_game_finished = self.chess_ai.is_game_over()


    def play_human_vs_ai(self):
        ai_move = None
        player_move = None
        is_player_turn = self.user_interactor.get_player_starts()
        while not(self.is_game_finished):
            if(is_player_turn):
                is_move_performed = False
                while not(is_move_performed):
                    #we can add move suggestion here, prompt user with question, if yes, call chessAI.getMoveSuggestion and display it

                    self.user_interactor.wait_for_player_confirmation()

                    player_move = ComputerVision.get_move_from_player(self.chess_ai.get_board())
                    
                    is_move_performed = self.chess_ai.play_move(play_move)
                    if(not(is_move_performed)):
                        self.user_interactor.display_try_again()
            else:
                ai_move = self.chess_ai.play_move_auto()
                self.perform_move_on_board(str(move))
            is_player_turn = not is_player_turn
            self.is_game_finished = self.chess_ai.is_game_over() 
        
        # check if draw
        
        #else see who won
        if(is_player_turn): #last move was done by AI
            print("AI won")
        else:
            print("Player won")

    def perform_move_on_board(self,move):
        #Go to start position of the move, magnet off
        path = ChessboardGraph.get_path_from_home_to_cell(move[:1])
        PhysicalBoard.move_motors(path,active_magnet=False)
        #Perform the move, magnet ON
        path = ChessboardGraph.get_path(move)
        PhysicalBoard.move_motors(path,active_magnet=True)
        #Go to home position when finished, magnet OFF
        path = ChessboardGraph.get_path(move[2:])
        PhysicalBoard.move_motors(path,active_magnet=False)

if __name__ == "__main__":
    instance = WizardsChess()
    instance.start()

        

    
