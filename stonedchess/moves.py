from dataclasses import dataclass
from typing import List, Tuple

from .board import Board


@dataclass
class Move:

    origin: Tuple[int, int]
    destination: Tuple[int, int]


def check_empy_spaces(board: Board, move: Move) -> bool:
    """Check if a move can be played without jumps"""

    # TODO


def generate(board: Board, file: int, rank: int) -> List[Move]:
    """Generate moves for the piece located ad the given square"""

    moves = []
    piece = board[file, rank]

    if piece is None:
        return moves

    for df, dr, steps, extend, jump in piece.movement.moves:

        cfile, crank = file + df, rank + dr

        # while in boundaries
        while (
            0 <= cfile < board.files
            and 0 <= crank < board.ranks
            and (steps > 0 or extend)
        ):

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
            cfile, crank = cfile + df, crank + dr
            steps -= 1

    return moves
