import cv2
import numpy as np


def get_move_from_player():
    cropXBegin = 190
    cropXEnd = 320
    cropYTop = 50
    cropYBottom = 70

    img = cv2.imread("chess.jpg") 

    lower_green = np.array([55,40,40])
    upper_green = np.array([68,255,255])

    lower_red = np.array([0,40,40])
    upper_red = np.array([1,255,255])

    res = ""
    board = img[cropYTop:img.shape[0] - cropYBottom , cropXBegin:img.shape[1] - cropXEnd, :]
    board = cv2.rotate(board, cv2.ROTATE_180)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow("output", board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for x in range(0, board.shape[0] - 8, board.shape[0]//8):
        for y in range(0, board.shape[1] - 8, board.shape[1]//8):      
            square = board[x : x + board.shape[0]//8, y : y + board.shape[1]//8, :]   
            hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)

            green_mask = cv2.inRange(hsv, lower_green, upper_green)
            red_mask = cv2.inRange(hsv, lower_red, upper_red)

            hasRed = np.sum(red_mask)
            hasGreen = np.sum(green_mask) 


            if hasGreen > 0 : 
                res += "x" 
            else:
                res += '.'
    print(res)
    return res