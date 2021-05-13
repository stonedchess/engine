from typing import Optional, Union

from .board import Board
from .player import Player
from .position import Position


class Game:
    """Game logic"""

    def __init__(self, board: Union[Board, Position]):
        self.board = board if isinstance(board, Board) else Board(board)

    @property
    def winner(self) -> Optional[Player]:
        """Check for a winner"""

        mop = {Player.white: 0, Player.black: 0}

        for file in range(self.board.size.file):
            for rank in range(self.board.size.rank):
                piece = self.board[file, rank]
                if piece and piece.mop:
                    mop[piece.owner] += 1

        if mop[Player.white] == 0:
            return Player.black

        if mop[Player.black] == 0:
            return Player.white
