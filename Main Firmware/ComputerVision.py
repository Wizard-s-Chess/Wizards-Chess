import numpy as np
import cv2
import numpy as np
from math import floor
import imutils
import os
import requests 
"""lower_green = np.array([36, 60, 60])
upper_green = np.array([86, 255, 255])
"""
lower_red = np.array([0, 70, 70])
upper_red = np.array([10, 255, 255])

lower_red2 = np.array([170, 70, 70])
upper_red2 = np.array([180, 255, 255])

lower_green = np.array([50, 70, 70])
upper_green = np.array([70, 255, 255])

"""lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])"""
class ComputerVision:
    def capture():
        url = "http://192.168.4.1/capture"
        req = requests.get(url)
        with open("chess.jpg", 'wb') as f:
            f.write(req.content)
            
    def convert_board(board):
        converted_board = str(board).replace("\n", "").replace(" ", "")
        green_pieces = "rqkbnp"
        red_pieces = "PQKBNR"
        for char in red_pieces:
            converted_board = converted_board.replace(char,"R")
        for char in green_pieces:
            converted_board = converted_board.replace(char,"G")
        return converted_board

    def diff(previous_board, next_board):
        previous_string = ComputerVision.convert_board(previous_board)
        next_string = ComputerVision.convert_board(next_board)[::-1]
        diff = [i for i in range(len(previous_string)) if previous_string[i] != next_string[i]]
        print(previous_string)
        print(next_string)
        if (len(diff) != 2):
            return ""
        if previous_string[diff[0]] == '.':
            diff = list(reversed(diff))
        print(diff)
        initial_position = str(chr((diff[0]%8) + 97) + str(abs(diff[0]//8 - 8)))
        final_position = str(chr((diff[1]%8) + 97) + str(abs(diff[1]//8 - 8)))
        return initial_position + final_position
        
    #returns the move object from the camera
    def get_player_move_from_camera(board):
        # Take 3 capture because of the delay
        for i in range(3):
            ComputerVision.capture()
        played_board = ComputerVision.process_image()
        #print(ComputerVision.convert_board(board))
        move_player = ComputerVision.diff(board, played_board)
        print(move_player)
        return move_player

    def try_range(square):
        """cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        cv2.imshow("output", square)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
        hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        hasGreen = np.sum(mask_green)

        mask_red =  cv2.inRange(hsv, lower_red, upper_red)
        hasRed = np.sum(mask_red)

        mask_red2 =  cv2.inRange(hsv, lower_red2, upper_red2)
        hasRed2 = np.sum(mask_red2)

        """print('red', hasRed, hasRed2)
        print('green', hasGreen)"""
        if hasRed > 7000 or hasRed2 > 7000:
            return 'R' 
        elif hasGreen > 7000:
            return 'G'
        else:
            return '.'

    def process_image():
        """cropXBegin = 125S
        cropXEnd = 50
        cropYTop = 250
        cropYBottom = 175"""
        cropXBegin = 140
        cropXEnd = 125
        cropYTop = 40
        cropYBottom = 75
        nline = 7
        ncol = 7

        img = cv2.imread("./chess.jpg")
        img = imutils.rotate_bound(img, -2)
        img = img[cropYTop:img.shape[0] - cropYBottom, cropXBegin:img.shape[1] - cropXEnd, :]     
        cv2.imshow("output", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        img = cv2.flip(img,1)
        img = cv2.rotate(img, cv2.ROTATE_180)
        img = cv2.flip(img, 0)

        x_list = []
        y_list = []
        if os.path.exists('./square_indices.txt'):
            with open('./square_indices.txt', 'r') as f:
                    is_x = True
                    for line in f:
                        coord = line[:-1]
                        if is_x:
                            x_list.append(int(coord))
                        else:
                            y_list.append(int(coord))
                        is_x = not is_x
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, (nline, ncol), None)
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            cv2.drawChessboardCorners(img, (7, 7), corners2, ret)
            cv2.namedWindow("output", cv2.WINDOW_NORMAL)
            cv2.imshow("output", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            with open('square_indices.txt', 'w') as f:
                for coord in corners2:
                    x_list.append(coord[0][1])
                    y_list.append(coord[0][0])
                    f.write("%d\n" % floor(coord[0][1]))
                    f.write("%d\n" % floor(coord[0][0]))

        board = img
        
        reduce_cell = 1

        cell_nbr = 0
        from_x = 0
        until_x = 0
        from_y = 0
        until_y = 0
        i = 0
        res = ""
        previous_x = []
        while cell_nbr < 8:
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x.append(until_x)
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1

        
        cell_nbr = 0
        i = 7
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x[j] = until_x
            j += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1

        #print(res)
        cell_nbr = 0
        i = 14
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x[j] = until_x
            j += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1

        cell_nbr = 0
        i = 21
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x[j] = until_x
            j += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1

        cell_nbr = 0
        i = 28
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x[j] = until_x
            j += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1

        cell_nbr = 0
        i = 35
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x[j] = until_x
            j += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1


        cell_nbr = 0
        i = 42
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = x_list[i - 1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = x_list[i]
                i += 1
            previous_x[j] = until_x
            j += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1

        cell_nbr = 0
        i = 42
        j = 0
        while cell_nbr < 8:
            from_x = previous_x[j]
            j += 1
            if cell_nbr % 8 == 0:
                from_y = 0
            else:
                from_y = y_list[i-1]
            if (cell_nbr + 1) % 8 == 0:
                until_y = board.shape[0]
                until_x = board.shape[1]
                i += 1
            else:
                until_y = y_list[i]
                until_x = board.shape[1]
                i += 1
            square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
            res += ComputerVision.try_range(square)
            cell_nbr += 1
        print('res' , res)
        return res

    

