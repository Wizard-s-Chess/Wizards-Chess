from serial import Serial


class CVP:
    def __init__(self):
        print("init bluetooth serial")
        if not (__debug__):
            self.serial_port = Serial("/dev/rfcomm0", 9600, timeout=None)

    def save_pre_movement_image(self):
        if __debug__:
            return
        # send request
        self.serial_port.write(bytes("p", "ascii"))
        # wait for acknowledgment
        self.serial_port.read(1)

    def get_next_move(self, legal_moves):
        if __debug__:
            return legal_moves[0]
        # send request
        self.serial_port.write(bytes("d", "ascii"))
        # wait for response
        changed_squares = self.serial_port.read(4)
        return self.get_move_from_diff(legal_moves, changed_squares)

    def get_move_combinations(self, list_squares):
        return [x + y for x in list_squares for y in list_squares if x != y]

    def get_move_from_diff(self, legal_moves, changed_squares):
        move = ""
        print("changed squares", changed_squares)
        # we could have a problem when player wants to make an illegal move
        if len(changed_squares) == 1:
            # check for legal moves and return it if there's exactly one that corresponds to the move we have but a problem might be that the person makes an illegal move and by chance the piece that detected the difference cna be moved in another way
            possible_moves = [a for a in legal_moves if (changed_squares[0] in a)]
            if len(possible_moves) == 1:
                move = possible_moves[0]
        if len(changed_squares) == 2 or len(changed_squares) == 3:
            move_combinations = self.get_move_combinations(changed_squares)
            possible_moves = [a for a in move_combinations if (a in legal_moves)]
            if len(possible_moves) == 1:
                move = possible_moves[0]
        if len(changed_squares) == 4:
            # should be an ideal case of detecting a castling move (=> verify if the moves correspond to a castling, if this is the case, return it)
            print()

        return move
