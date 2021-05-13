from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple, Union

from .movement import Movement
from .piece import Piece, std
from .player import Player
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

    @staticmethod
    def std():
        """Standard board"""

        board = Board(Position(8, 8))

        # white pieces
        board.add(
            (Position(0, 0), std.Rook(Player.white)),
            (Position(1, 0), std.Knight(Player.white)),
            (Position(2, 0), std.Bishop(Player.white)),
            (Position(3, 0), std.King(Player.white)),
            (Position(4, 0), std.Queen(Player.white)),
            (Position(5, 0), std.Bishop(Player.white)),
            (Position(6, 0), std.Knight(Player.white)),
            (Position(7, 0), std.Rook(Player.white)),
        )

        # black pieces
        board.add(
            (Position(0, 7), std.Rook(Player.black)),
            (Position(1, 7), std.Knight(Player.black)),
            (Position(2, 7), std.Bishop(Player.black)),
            (Position(3, 7), std.King(Player.black)),
            (Position(4, 7), std.Queen(Player.black)),
            (Position(5, 7), std.Bishop(Player.black)),
            (Position(6, 7), std.Knight(Player.black)),
            (Position(7, 7), std.Rook(Player.black)),
        )

        # white pawns
        for i in range(8):
            board[i, 1] = std.Pawn(Player.white)

        # black pawns
        for i in range(8):
            board[i, 6] = std.Pawn(Player.black)

        return board

    def __init__(self, size: Position):
        self.squares = [Square() for _ in range(size.file * size.rank)]
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

    def moves(self, position: Position) -> List[Move]:
        """Generate moves for a cell"""

        origin = Position(position.file, position.rank)
        piece = self[position]
        if piece is None:
            return []

        def explore(graph: Movement.Node, position: Position) -> List[Move]:
            """Explore graph for moves"""

            moves = []
            repeat = graph.repeat
            direction = graph.direction.adapt(self[origin].owner).value

            if graph.extend:

                repeat = 0
                pointer = Position(position.file, position.rank)

                while pointer in self:
                    pointer += direction
                    repeat += 1

            for i in range(repeat):

                for _ in range(graph.amount):

                    position += direction

                    if position not in self:
                        break

                    if self[position] is not None and not graph.jumps:
                        break

                else:

                    if len(graph.branches) == 0:
                        moves.append(Move(origin, position))

                    for branch in graph.branches:
                        moves += explore(branch, position)

                    continue

                # captures
                if (
                    self[position] is not None
                    and self[position].owner == self[origin].owner.opponent
                ):
                    moves.append(Move(origin, position, MoveType.capture))

                break

            return moves

        return explore(piece.movement.graph, position)
