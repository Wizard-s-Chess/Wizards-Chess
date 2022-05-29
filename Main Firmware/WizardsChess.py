
import ChessboardGraph
import PhysicalBoard
import UserInteractor
from ComputerVision import ComputerVision
import ChessAI
import time
class WizardsChess:
    def __init__(self):
        print("initializing")
        self.chess_ai = ChessAI.ChessAI()
        self.user_interactor = UserInteractor.UserInteractor()
        self.physical_board = PhysicalBoard.PhysicalBoard()
        self.is_game_finished = False
        self.path_generator = ChessboardGraph.PathGenerator()
        
        
    def start(self):
        self.is_game_finished = False
        player_mode = True#self.user_interactor.get_game_mode()
        #level = self.user_interactor.choose_ai_level()
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
                (ai_1_move,is_capture) = self.chess_ai.play_move_auto()
                print("ai 1 ",ai_1_move)
                self.perform_move_on_board(str(ai_1_move),is_capture)
                print(self.chess_ai.get_board())
            else:
                (ai_2_move,is_capture) = self.chess_ai.play_move_auto()
                print("ai 2 ",ai_2_move)
                #self.perform_move_on_board(str(ai_2_move),is_capture)
            is_ai_1_turn = not is_ai_1_turn
            self.is_game_finished = self.chess_ai.is_game_over()

    def play_human_vs_ai(self):
        ai_move = None
        player_move = None
        #is_player_turn = self.user_interactor.get_player_starts()
        is_player_turn = False
        while not(self.is_game_finished):
            if(is_player_turn):
                is_move_performed = False
                while not(is_move_performed):
                    #we can add move suggestion here, prompt user with question, if yes, call chessAI.getMoveSuggestion and display it

                    #self.user_interactor.wait_for_player_confirmation()
                    input("press when played")

                    player_move = ComputerVision.get_player_move_from_camera(self.chess_ai.get_board())
                    (is_move_performed,is_capture) = self.chess_ai.play_move(player_move)
                    print(player_move,is_move_performed)
                    #if(not(is_move_performed)):
                    #    self.user_interactor.display_try_again()
            else:
                (ai_move,is_capture) = self.chess_ai.play_move_auto()
                self.perform_move_on_board(str(ai_move),is_capture)
            is_player_turn = not is_player_turn
            self.is_game_finished = self.chess_ai.is_game_over() 
        
        # check if draw
        
        #else see who won
        if(is_player_turn): #last move was done by AI
            print("AI won")
        else:
            print("Player won")

    def perform_move_on_board(self,move,is_capture):
        if(is_capture):#eliminate captured
            #Go to end position of piece (corresponding to start position of piece to eliminate)
            path = self.path_generator.get_path_to_cell(move[2:])
            print("going to",move[2:]," to gutter")
            self.physical_board.move_motors(path,active_magnet = False)
            path = self.path_generator.get_path_from_cell_to_gutter(move[2:])
            
            self.physical_board.move_motors(path,active_magnet = True)
            print(move[2:],"in gutter")

        #Go to start position of the move, magnet off
        path = self.path_generator.get_path_to_cell(move[:2])
        print("going to",move[:2])
        self.physical_board.move_motors(path,active_magnet=False)
        #Perform the move, magnet ON
        path = self.path_generator.get_path_move(move)
        print("taking to",move[2:])
        self.physical_board.move_motors(path,active_magnet=True)

if __name__ == "__main__":
    instance = WizardsChess()
    instance.start()

        

    
