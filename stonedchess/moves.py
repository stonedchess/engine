from dataclasses import dataclass
from typing import List, Tuple

from .board import Board


@dataclass
class Move:

    origin: Tuple[int, int]
    destination: Tuple[int, int]


def generate(board: Board, file: int, rank: int) -> List[Move]:
    """Generate moves for the piece located ad the given square"""

    moves = []
    piece = board[file, rank]

    if piece is None:
        return moves

    for df, dr in piece.movement:

        cfile = file + df
        crank = rank + dr

        # while in boundaries
        while 0 <= cfile < board.files and 0 <= crank < board.ranks:

            # if destination is occupied
            if board[cfile, crank] is not None:

                # stop if the piece cannot jumps
                if not piece.jumping:
                    break

            else:

                # create move
                move = Move((file, rank), (cfile, crank))
                moves.append(move)

            # update pointer
            cfile += df
            crank += dr

    return moves
