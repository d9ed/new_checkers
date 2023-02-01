from game_objects.board import Board
from game_objects.player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.p1 = Player("r")
        self.p2 = Player("b")
        self.is_running = True



    def run(self):
        while self.is_running:
            self.p1.play_turn()
            self.p2.play_turn()
            self.board.print_board()
            # row_index = Player.validate_input(
            #                                   list_to_validate= self.board.state,
            #                                   message = "please enter your chosen row from 0-7.\n",
            #                                   name_of_list = "board",
            #                                   piece_color=  cur_player)
            # row = self.board.state[row_index]
            # piece_index = Player.validate_input(
            #                                     list_to_validate = row,
            #                                     message = "please choose a piece on this row.\n",
            #                                     name_of_list = "row",
            #                                     piece_color = cur_player)
            # # while True:
            #     row = input()
            #     col = input()
            #     cur_cell = self.board.state[row][col]
            #     if isinstance(cell, Piece) and cell.color == player.color:
            #         break
            #     print()
            # # while True:
            #     row = input()
            #     col = input()
            #     next_cell = self.board.state[row][col]
            #     if isempty
            #         break
            #     print()
            cur_cell = ""
            # next_cell = Piece(cur_player.color)

            # if cur_player == self.p1:
            #     next_row = self.board.state[row_index + 1]
            # else:
            #     next_row = self.board.state[row_index - 1]
            # next_row_index = Player.validate_input(next_row, "please choose where you want to move your piece, from 0-7.\n",
            #                                 "next_row", cur_player)
            # next_row[next_row_index] = Piece(cur_player.color)
            # row[piece_index] = " "
            # cur_player = Game.change_player(cur_player, self.p1, self.p2)
            # break
