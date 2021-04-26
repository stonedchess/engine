from typing import List

from .board import Board
from .movement import Move
from .piece import Piece


def render(board: Board, moves: List[Move] = "", newline: str = "\n") -> str:
    """Render the board to ascii characters"""

    sep = "+---" * board.files + "+"
    moves = [move.destination for move in moves]
    lines = [sep]

    for rank in range(board.ranks):

        line = []
        for file in range(board.files):
            piece = board[file, rank] or Piece(" ")
            move = "." if (file, rank) in moves else " "
            line.append(f"{move}{piece.char} ")

        line = "|".join(["", *line, ""])
        lines += [line, sep]

    return newline.join(lines)
