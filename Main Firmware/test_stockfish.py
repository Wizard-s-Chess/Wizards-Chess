import ChessAI


chess_ai = ChessAI.ChessAI()
ai_move = None
player_move = None
is_player_turn = True
is_game_finished = False
while not(is_game_finished):
    if(is_player_turn):
        print(chess_ai.get_board())
        is_move_performed = False
        while not(is_move_performed):
            player_move = input("Type your move: ")
            (is_move_performed,is_capture) = chess_ai.play_move(player_move)
            print(player_move,is_move_performed)
            if(not(is_move_performed)):
                print("move not performed")
    else:
        (ai_move,is_capture) = chess_ai.play_move_auto()
        print("AI Played",str(ai_move))
        #print(chess_ai.get_board())
    is_player_turn = not is_player_turn
    is_game_finished = chess_ai.is_game_over()
print("game over")