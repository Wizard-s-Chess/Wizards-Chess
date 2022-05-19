import cv2
import numpy as np


def get_move_from_player():
    cropXBegin = 190
    cropXEnd = 320
    cropYTop = 50
    cropYBottom = 65 

    img = cv2.imread("./chess.jpg") 

    lower_green = np.array([36, 60, 60])
    upper_green = np.array([86, 255, 255])

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    res = ""
    board = img[cropYTop:img.shape[0] - cropYBottom, cropXBegin:img.shape[1] - cropXEnd, :]
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow("output", board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for x in range(0, board.shape[0] - 8, board.shape[0]//8):
        for y in range(0, board.shape[1] - 8, board.shape[1]//8):      
            square = board[x : x + board.shape[0]//8, y : y + board.shape[1]//8, :]    
            """cv2.imshow("output", square)
            cv2.waitKey(0)
            cv2.destroyAllWindows()"""
            hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)

            mask_green =  cv2.inRange(hsv, lower_green, upper_green)
            hasGreen = np.sum(mask_green)

            mask_red =  cv2.inRange(hsv, lower_red, upper_red)
            hasRed = np.sum(mask_red)

            print("red : ", hasRed)

            if hasGreen > 15000 or hasRed > 500:
                res += "x" 
            else:
                res += '.'
    print(res)
    return res