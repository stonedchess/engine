from typing import List

from .board import Board, Move
from .piece import Piece
from .position import Position


def render(board: Board, moves: List[Move] = [], newline: str = "\n") -> str:
    """Render the board to ascii characters"""

    sep = "+---" * board.size.file + "+"
    moves = [move.destination for move in moves]
    lines = [sep]

    for rank in range(board.size.rank):

        line = []
        for file in range(board.size.file):
            piece = board[file, rank] or Piece(" ")
            move = "." if Position(file, rank) in moves else " "
            line.append(f"{move}{piece.char} ")

        line = "|".join(["", *line, ""])
        lines += [line, sep]

    return newline.join(lines)
