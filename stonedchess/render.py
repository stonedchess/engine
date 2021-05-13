from typing import List

from .board import Board, Move
from .position import Position


def render(board: Board, moves: List[Move] = [], newline: str = "\n") -> str:
    """Render the board to ascii characters"""

    sep = "+---" * board.size.file + "+"
    moves = {move.destination: move for move in moves}
    lines = [sep]

    for rank in range(board.size.rank):

        line = []
        for file in range(board.size.file):
            piece = board[file, rank]
            char = piece.char[piece.owner.value] if piece else " "
            move = moves.get(Position(file, rank))
            move = [".", "x"][move.type.value] if move else " "
            line.append(f"{move}{char} ")

        line = "|".join(["", *line, ""])
        lines += [line, sep]

    return newline.join(lines)
