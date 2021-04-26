from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

from .movement import Movement
from .piece import Piece
from .position import Position


@dataclass
class Move:

    origin: Position
    destination: Position


@dataclass
class Square:

    piece: Optional[Piece] = None


class Board:
    """Board states holder"""

    def __init__(self, size: Position):
        self.squares = [Square() for _ in range(size.file * size.rank)]
        self.size = size

    def add(self, *pieces: Tuple[int, int, Piece]):
        """Add pieces to the board"""

        for file, rank, piece in pieces:
            self[file, rank] = piece

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

    def moves(self, file: int, rank: int) -> List[Move]:
        """Generate moves for a cell"""

        piece = self[file, rank]
        if piece is None:
            return []

        def explore(graph: Movement.Node, position: Position) -> List[Move]:
            """Explore graph for moves"""

            ok = True
            old = Position(position.file, position.rank)

            for i in range(graph.amount):

                position += graph.direction.value
                if self[position] is not None and not graph.jumps:
                    ok = False
                    break

            if not ok:
                return []

            moves = []

            if len(graph.branches) == 0:
                moves.append(Move(old, position))

            for branch in graph.branches:
                moves += explore(branch, position)

            return moves

        return explore(piece.movement.graph, Position(file, rank))
