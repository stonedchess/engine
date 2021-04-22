class Piece:
    """Piece"""

    def __init__(self, file: int, rank: int, char: str = "?"):
        self.file = file
        self.rank = rank
        self.char = char
