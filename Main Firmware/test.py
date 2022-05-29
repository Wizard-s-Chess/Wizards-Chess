from ComputerVision import ComputerVision
import ChessAI
chess_ai = ChessAI.ChessAI()
player_move = ComputerVision.get_player_move_from_camera(chess_ai.get_board())
(is_move_performed,is_capture) = chess_ai.play_move(player_move)
print(player_move,is_move_performed)