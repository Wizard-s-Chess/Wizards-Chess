
from ComputerVision import ComputerVision

for i in range(3):
    ComputerVision.capture()
played_board = ComputerVision.process_image()
for i in range(8):
    print(played_board[i,i+8])
