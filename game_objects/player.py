from game_objects.pieces import Piece
from game_objects.board import Board


class Player:
    def __init__(self, color):
        self.color = color
        self.rule = MovementRules

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
            else:
                print("Invalid input. Please try again")
        return int(row) - 1, int(col) - 1

    def move(self, board, cell, piece_row, piece_col):
        while True:
            print("Please choose where you'd like to move")
            to_row, to_col = self.input_cell()
            future_cell = board.state[to_row][to_col]

            if not self.rule.same_cell(cell, future_cell):
                board.state[piece_row][piece_col] = " "
                board.state[to_row][to_col] = self.color
                break

    def play_turn(self, board):
        print("current player:", self.color)

        while True:
            print("Please choose your piece")
            piece_row, piece_col = self.input_cell()
            cell = board.state[piece_row][piece_col]
            if self.rule.piece_belongs_to_player(self, cell, Piece):
                break

        self.move(board, cell, piece_row, piece_col)


class MovementRules(Player):
    @staticmethod
    def piece_belongs_to_player(self, cell, Piece):
        if isinstance(cell, Piece) and cell.color == self.color:
            return True
        print("sorry, your piece must be the same color.")
        return False

    @staticmethod
    def same_cell(cell, future_cell):
        if cell == future_cell:
            print("Invalid piece, please try again")
            return True
