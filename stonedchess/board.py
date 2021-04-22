from dataclasses import dataclass
from typing import List, Optional, Tuple

from .piece import Piece


@dataclass
class Square:

    piece: Optional[Piece] = None


class Board:
    """Board states holder"""

    def __init__(self, files: int, ranks: int, pieces: List[Piece]):
        self.files = files
        self.ranks = ranks
        self.pieces = pieces

        self.squares = [Square() for _ in range(self.files * self.ranks)]
        for piece in self.pieces:
            self[piece.file, piece.rank] = piece

    def index(self, file: int, rank: int) -> int:
        """Get square index, given his file and rank"""

        return rank * self.files + file

    def __getitem__(self, coordinates: Tuple[int, int]) -> Square:
        """Retrieve square by slice [file, rank]"""

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
