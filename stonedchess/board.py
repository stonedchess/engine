from dataclasses import dataclass
from typing import Optional, Tuple

from .piece import Piece


@dataclass
class Square:

    piece: Optional[Piece] = None


class Board:
    """Board states holder"""

    def __init__(self, files: int, ranks: int):
        self.files = files
        self.ranks = ranks

        self.squares = [Square() for _ in range(self.files * self.ranks)]

    def add(self, *pieces: Tuple[int, int, Piece]):
        """Add pieces to the board"""

        for file, rank, piece in pieces:
            self[file, rank] = piece

        return self

    def index(self, file: int, rank: int) -> int:
        """Get square index, given his file and rank"""

        return rank * self.files + file

    def __getitem__(self, coordinates: Tuple[int, int]) -> Square:
        """Retrieve piece by slice [file, rank]"""

        return self.squares[self.index(coordinates[0], coordinates[1])].piece

    def __setitem__(self, coordinates: Tuple[int, int], piece: Piece):
        """Set piece by slice [file, rank]"""

        self.squares[self.index(coordinates[0], coordinates[1])].piece = piece

    def render(self, newline: str = "\n") -> str:
        """Render a board as ascii characters"""

        sep = "+---" * self.files + "+"
        lines = [sep]

        for rank in range(self.ranks):

            line = []
            for file in range(self.files):
                piece = self[file, rank]
                piece = piece.char if piece is not None else " "
                line.append(f" {piece} ")

            line = "|".join(["", *line, ""])
            lines.append(line)
            lines.append(sep)

        return newline.join(lines)
