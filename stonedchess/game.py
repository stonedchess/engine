from typing import Union

from .board import Board
from .position import Position


class Game:
    """Game logic"""

    def __init__(self, board: Union[Board, Position]):
        self.board = board if isinstance(board, Board) else Board(board)
        self.winner = None
