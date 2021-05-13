from typing import List

from .board import Board, Move
from .position import Position


def render(board: Board, moves: List[Move] = [], newline: str = "\n") -> str:
    """Render the board to ascii characters"""

    sep = "+---" * board.size.file + "+"
    origins = {move.origin for move in moves}
    moves = {move.destination: move for move in moves}
    lines = [sep]

    for rank in range(board.size.rank):

        line = []
        for file in range(board.size.file):
            piece = board[file, rank]
            char = piece.char[piece.owner.value] if piece else " "
            move = moves.get(Position(file, rank))
            move = [".", "x"][move.type.value] if move else " "
            move = "+" if Position(file, rank) in origins else move
            mop = piece.mop if piece else False
            mop = "!" if mop else " "
            line.append(f"{move}{char}{mop}")

        line = "|".join(["", *line, ""])
        lines += [line, sep]

    return newline.join(lines)
