
class Piece:
    def __init__(self, color, role="default"):
        self.role = role
        self.color = color

    def __str__(self):
        return f"{self.color}"
