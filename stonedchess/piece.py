class Movements:
    """Standar movements"""

    rook = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    bishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    horse = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]


class Piece:
    """Piece"""

    movement = Movements.horse
    jumping = False

    def __init__(self, char: str = "?"):
        self.char = char
