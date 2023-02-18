# import pieces
from game_objects.pieces import Piece


class Board:
    def __init__(self):
        self.state = [
            [Piece('r'), ' ', Piece('r'), ' ', Piece('r'), ' ', Piece('r'), ' '],
            [' ', Piece('r'), ' ', Piece('r'), ' ', Piece('r'), ' ', Piece('r')],
            [Piece('r'), ' ', Piece('r'), ' ', Piece('r'), ' ', Piece('r'), ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', Piece('b'), ' ', Piece('b'), ' ', Piece('b'), ' ', Piece('b')],
            [Piece('b'), ' ', Piece('b'), ' ', Piece('b'), ' ', Piece('b'), ' '],
            [' ', Piece('b'), ' ', Piece('b'), ' ', Piece('b'), ' ', Piece('b')]
        ]

    # def move(self, chosen_cell, move_to_cell):
    #     chosen_cell = " "
    #     move_to_cell
    #     return

    def print_board(self, num=33):
        print("—"*num)
        for row in self.state:
            show_row = ""
            for col in row:
                show_col = f"| {col} "
                show_row += show_col
            print(show_row+"|")
        print("—"*num)

# class MovementLogic():
#     def __init__(self):
