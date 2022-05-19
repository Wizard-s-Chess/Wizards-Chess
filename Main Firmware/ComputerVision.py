import cv2
import numpy as np
import requests
class ComputerVision:
    def capture():
        url = "http://192.168.4.1/capture"
        req = requests.get(url)
        with open("chess.jpg", 'wb') as f:
            f.write(req.content)
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
    #returns the move object from the camera
    def get_player_move_from_camera(board):
        capture()
        played_board = process_image()
        print(convert_board(board))
        move_player = diff(board, played_board)
        print(move_player)
        return move_player

    def process_image():
        cropXBegin = 102
        cropXEnd = 112
        cropYTop = 0
        cropYBottom = 45

        img = cv2.imread("chess.jpg") 

        lower_green = np.array([50,40,40])
        upper_green = np.array([65,255,255])

        lower_blue = np.array([100,150,0])
        upper_blue = np.array([140,255,255])

        lower_red = np.array([0, 70, 50])
        upper_red = np.array([15,255,255])

        lower_red2 = np.array([165, 70, 50])
        upper_red2 = np.array([180,255,255])

        res = ""
        board = img[cropYTop:img.shape[0] - cropYBottom - 10, cropXBegin:img.shape[1] - cropXEnd, :]
        board = cv2.rotate(board, cv2.ROTATE_180)
        cv2.imshow("board", board)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        for x in range(0, board.shape[0] - 8, board.shape[0]//8):
            for y in range(0, board.shape[1] - 8, board.shape[1]//8):      
                square = board[x : x + board.shape[0]//8, y : y + board.shape[1]//8, :]    

                hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)

                mask_green = cv2.inRange(hsv, lower_green, upper_green)
                blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
                red_mask = cv2.inRange(hsv, lower_red, upper_red)
                red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

                hasGreen = np.sum(mask_green)
                hasBlue = np.sum(blue_mask)
                hasRed = np.sum(red_mask)
                hasRed2 = np.sum(red_mask2)


                if hasRed2 > 0 or hasRed > 0: 
                    res += "x" 
                else:
                    res += '.'
        print(res)
        return res