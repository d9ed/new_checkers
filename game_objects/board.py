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

    def print_board(self):
        for row in self.state:
            for col in row:
                print(col, end=" ")
            print()
