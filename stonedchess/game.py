from typing import List, Optional, Union

from .board import Board, Move, MoveType
from .movement import Movement
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


def moves(game: Game, position: Position) -> List[Move]:
    """Generate moves for a position"""

    origin = Position(position.file, position.rank)
    piece = game.board[origin]

    if piece is None:
        return []

    def explore(graph: Movement.Node, position: Position) -> List[Move]:
        """Explore a movement graph for moves"""

        moves = []
        repeat = graph.repeat
        direction = graph.direction.adapt(piece.owner).value

        if graph.extend:

            repeat = 0
            pointer = Position(position.file, position.rank)

            while pointer in game.board:
                pointer += direction
                repeat += 1

        for i in range(repeat):

            for _ in range(graph.amount):

                position += direction

                if position not in game.board:
                    break

                if game.board[position] is not None and not graph.jumps:
                    break

            else:

                if len(graph.branches) == 0:
                    moves.append(Move(origin, position))

                for branch in graph.branches:
                    moves += explore(branch, position)

                continue

            if (
                position in game.board
                and game.board[position] is not None
                and game.board[position].owner == piece.owner.opponent
            ):
                moves.append(Move(origin, position, MoveType.capture))

            break

        return moves

    return explore(piece.movement.graph, position)
