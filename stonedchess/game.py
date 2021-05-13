from typing import List, Optional, Union

from .board import Board, Move
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

        for position in self.board.size:
            piece = self.board[position]
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

    def explore(
        graph: Movement.Node,
        position: Position,
        force_captures: bool = False,
    ) -> List[Move]:
        """Explore a movement graph for moves"""

        moves = []
        repeat = graph.repeat

        # adapt the direction to the color
        # -> change south with north
        direction = graph.direction.adapt(piece.owner).value

        # compute the extended repeat count
        if graph.extend:

            repeat = 0
            pointer = Position(position.file, position.rank)

            # iterate until the pointer reaches the edge of the board
            while pointer in game.board:
                pointer += direction
                repeat += 1

        for i in range(repeat):

            for _ in range(graph.amount):

                # update current position
                position += direction

                # check if the position is in the board boundaries
                if position not in game.board:
                    break

                # check if the position is occupied
                # -> if the piece cannot jump, break
                if game.board[position] is not None and not graph.jumps:
                    break

            # reached when the for loop terminate
            # without any break, hence without any
            # abnormal interruption
            else:

                # if we reached a leaf of the grapf,
                # add the move to the list of moves
                if len(graph.branches) == 0 and not force_captures:
                    moves.append(Move(origin, position))

                # if there are sub branches, iterate
                # over them and add the new moves
                for branch in graph.branches:
                    moves += explore(branch, position, force_captures)

                # continue directly to the next repeat step
                # avoifing the "interrupted behavior" execution
                continue

            # interrupted behavior checks.
            # if the piece is occupied and is of different color,
            # add the capture to the list of moves
            if (
                position in game.board
                and game.board[position] is not None
                and game.board[position].owner == piece.owner.opponent
                and graph.capture
            ):
                moves.append(Move(origin, position))

            # the path is interrupted, hence
            # break and return
            break

        return moves

    movement = piece.movement

    if not isinstance(movement, Movement):
        index = min(len(movement) - 1, piece.moves_count)
        movement = movement[index]

    moves = explore(movement.graph, position)

    if piece.capture is not None:
        moves += explore(piece.capture.graph, position, True)

    return moves
