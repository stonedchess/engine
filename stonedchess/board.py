from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple, Union

from .piece import Piece
from .position import Position


class MoveType(Enum):

    move = 0
    capture = 1


@dataclass
class Move:

    origin: Position
    destination: Position

    type: MoveType = MoveType.move


@dataclass
class Square:

    piece: Optional[Piece] = None


class Board:
    """Board states holder"""

    def __init__(self, size: Position):
        self.squares = [Square() for _ in size]
        self.history = []
        self.size = size

    def add(self, *pieces: Tuple[int, int, Piece]):
        """Add pieces to the board"""

        for position, piece in pieces:
            self[position] = piece

        return self

    def index(self, position: Position) -> int:
        """Get square index, given his file and rank"""

        return position.rank * self.size.file + position.file

    def __getitem__(
        self,
        position: Union[Tuple[int, int], Position],
    ) -> Optional[Piece]:
        """Retrieve piece by slice [file, rank]"""

        position = (
            position
            if isinstance(position, Position)
            else Position(position[0], position[1])
        )

        return self.squares[self.index(position)].piece

    def __setitem__(
        self,
        position: Union[Tuple[int, int], Position],
        piece: Piece,
    ):
        """Set piece by slice [file, rank]"""

        position = (
            position
            if isinstance(position, Position)
            else Position(position[0], position[1])
        )

        self.squares[self.index(position)].piece = piece

    def __contains__(self, position: Position) -> bool:
        """Check if a position is inside the board"""

        return 0 <= self.index(position) < len(self.squares)

    def move(self, move: Move):
        """Make a move"""

        self.history.append([move, self[move.destination], self[move.origin]])
        self[move.destination] = self[move.origin]
        self[move.origin] = None

    def undo(self):
        """Undo last move"""

        move, destination, origin = self.history.pop()
        self[move.destination] = destination
        self[move.origin] = origin
