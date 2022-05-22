from cgi import test
from matplotlib.pyplot import xlim, ylim
import numpy as np
import cv2
import numpy as np
from math import floor

cropXBegin = 135
cropXEnd = 149
cropYTop = 55
cropYBottom = 65 
nline = 7
ncol = 7

img = cv2.imread("./chessWebcam.jpeg")
img = img[cropYTop:img.shape[0] - cropYBottom, cropXBegin:img.shape[1] - cropXEnd, :]
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, (nline, ncol), None)
corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
cv2.drawChessboardCorners(img, (7, 7), corners2, ret)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_green = np.array([36, 60, 60])
upper_green = np.array([86, 255, 255])

lower_red = np.array([0, 30, 30])
upper_red = np.array([15, 255, 255])

res = ""
board = img
#board = cv2.rotate(board, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("output", board)
cv2.waitKey(0)
cv2.destroyAllWindows()

x_list = []
y_list = []
for coord in corners2:
    x_list.append(coord[0][1])
    y_list.append(coord[0][0])

print(corners2)

reduce_cell = 1

cell_nbr = 0
from_x = 0
until_x = 0
from_y = 0
until_y = 0
i = 0

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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

cell_nbr = 0
i = 7
while cell_nbr < 8:
    from_x = x_list[0]
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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

cell_nbr = 0
i = 14
while cell_nbr < 8:
    from_x = x_list[7]
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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

cell_nbr = 0
i = 21
while cell_nbr < 8:
    from_x = x_list[14]
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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

cell_nbr = 0
i = 28
while cell_nbr < 8:
    from_x = x_list[21]
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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

cell_nbr = 0
i = 35
while cell_nbr < 8:
    from_x = x_list[28]
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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1


cell_nbr = 0
i = 42
while cell_nbr < 8:
    from_x = x_list[35]
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
    square = board[floor(from_x) + reduce_cell : floor(until_x) - reduce_cell, floor(from_y) + reduce_cell : floor(until_y) - reduce_cell, :]
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

cell_nbr = 0
i = 42
while cell_nbr < 8:
    from_x = x_list[42]
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
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1


print(res)
