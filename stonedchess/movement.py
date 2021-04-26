from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple


@dataclass
class Move:

    origin: Tuple[int, int]
    destination: Tuple[int, int]


class Direction(Enum):
    """Movement directions"""

    right = (1, 0)
    left = (-1, 0)
    top = (0, 1)
    bottom = (0, -1)

    right_top = (1, 1)
    right_bottom = (1, -1)
    left_top = (-1, 1)
    left_bottom = (-1, -1)


class Movement:
    """Piece movement"""

    def __init__(self):
        self.paths = [[]]

    def walk(self, dir: Direction, amount: int = 1):
        """"""

        steps = [dir.value] * amount
        self.paths = [path + steps for path in self.paths]
        return self

    def split(self, *branches):
        """"""

        paths = []

        for movement in branches:
            for branch in movement.paths:
                paths += [path + branch for path in self.paths]

        self.paths = paths
        return self


def generate(board, file: int, rank: int) -> List[Move]:
    """Generate moves on the baord"""

    moves = []
    piece = board[file, rank]

    if piece is None:
        return moves

    for steps in piece.movement.paths:

        ok = True
        c_file = file
        c_rank = rank

        for df, dr in steps:

            c_file += df
            c_rank += dr

            if board[c_file, c_rank] is not None:
                ok = False
                break

        if ok:
            move = Move((file, rank), (c_file, c_rank))
            moves.append(move)

    return moves
