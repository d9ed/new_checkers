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
            self.board.print_board()
            self.p1.play_turn(self.board)
            self.p2.play_turn(self.board)
            self.board.print_board()
