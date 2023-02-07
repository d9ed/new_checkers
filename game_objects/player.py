from game_objects.pieces import Piece


class Player:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"{self.color}"

    @staticmethod
    def is_valid(input_value):
        if input_value.isdigit() and (1 <= int(input_value) <= 8):
            return True
        return False

    def input_cell(self):
        while True:
            row = input("please enter a row (1-8):\n")
            col = input("please enter a cell (1-8):\n")
            if self.is_valid(row) and self.is_valid(col):
                break
        return int(row) - 1, int(col) - 1

    def play_turn(self, board):
        while True:
            piece_row, piece_col = self.input_cell()
            cell = board.state[piece_row][piece_col]
            if isinstance(cell, Piece) and cell.color == self.color:
                break
