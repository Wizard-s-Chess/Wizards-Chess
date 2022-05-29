from cgi import test
import re
from matplotlib.pyplot import xlim, ylim
import numpy as np
import cv2
import numpy as np
from math import floor
import imutils
import os

cropXBegin = 130
cropXEnd = 120
cropYTop = 500
cropYBottom = 70 
nline = 7
ncol = 7

img = cv2.imread("./chess.jpg")
img = imutils.rotate_bound(img, -3)
img = img[cropYTop:img.shape[0] - cropYBottom, cropXBegin:img.shape[1] - cropXEnd, :]
#img = cv2.rotate(img, cv2.ROTATE_180)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


"""lower_green = np.array([36, 60, 60])
upper_green = np.array([86, 255, 255])
"""
lower_red = np.array([0, 60, 60])
upper_red = np.array([10, 255, 255])

lower_red2 = np.array([170, 60, 60])
upper_red2 = np.array([180, 255, 255])

lower_green = np.array([50, 60, 60])
upper_green = np.array([70, 255, 255])

"""lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])"""

board = img
cv2.imshow("output", board)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
    ret, corners = cv2.findChessboardCorners(gray, (nline, ncol), None)
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

print(list(zip(x_list, y_list)))

reduce_cell = 2

cell_nbr = 0
from_x = 0
until_x = 0
from_y = 0
until_y = 0
i = 0

def try_range(square):
    global res
    hsv = cv2.cvtColor(square, cv2.COLOR_BGR2HSV)

    mask_green =  cv2.inRange(hsv, lower_green, upper_green)
    hasGreen = np.sum(mask_green)

    mask_red =  cv2.inRange(hsv, lower_red, upper_red)
    hasRed = np.sum(mask_red)

    mask_red2 =  cv2.inRange(hsv, lower_red2, upper_red2)
    hasRed2 = np.sum(mask_red2)

    print("red : ", hasRed, hasRed2)
    print("green : ", hasGreen)

    if hasGreen > 750 or hasRed > 500 or hasRed2 > 500:
        res += "x" 
    else:
        res += '.'

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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

print(res)
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1

print(res)
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
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
    try_range(square)
    cv2.imshow("output", square)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cell_nbr += 1


print("res ", res)
