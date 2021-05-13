from .board import Board
from .movement import Direction, Movement
from .piece import Piece
from .player import Player
from .position import Position


class Rook(Piece):

    char = ["♖", "♜", " "]
    movement = Movement().split(
        Movement().walk(Direction.N, extend=True),
        Movement().walk(Direction.S, extend=True),
        Movement().walk(Direction.W, extend=True),
        Movement().walk(Direction.E, extend=True),
    )


class Bishop(Piece):

    char = ["♗", "♝", " "]
    movement = Movement().split(
        Movement().walk(Direction.NE, extend=True),
        Movement().walk(Direction.SE, extend=True),
        Movement().walk(Direction.NW, extend=True),
        Movement().walk(Direction.SW, extend=True),
    )


class Knight(Piece):

    char = ["♘", "♞", " "]
    movement = Movement().split(
        Movement(jumps=True)
        .walk(Direction.N, amount=2)
        .split(
            Movement().walk(Direction.E),
            Movement().walk(Direction.W),
        ),
        Movement(jumps=True)
        .walk(Direction.S, amount=2)
        .split(
            Movement().walk(Direction.E),
            Movement().walk(Direction.W),
        ),
        Movement(jumps=True)
        .walk(Direction.W, amount=2)
        .split(
            Movement().walk(Direction.N),
            Movement().walk(Direction.S),
        ),
        Movement(jumps=True)
        .walk(Direction.E, amount=2)
        .split(
            Movement().walk(Direction.N),
            Movement().walk(Direction.S),
        ),
    )


class Pawn(Piece):

    char = ["♙", "♟︎", " "]
    movement = Movement().walk(Direction.N)


class Queen(Piece):

    char = ["♕", "♛", " "]
    movement = Movement().split(
        Movement().walk(Direction.N, extend=True),
        Movement().walk(Direction.S, extend=True),
        Movement().walk(Direction.W, extend=True),
        Movement().walk(Direction.E, extend=True),
        Movement().walk(Direction.NE, extend=True),
        Movement().walk(Direction.SE, extend=True),
        Movement().walk(Direction.NW, extend=True),
        Movement().walk(Direction.SW, extend=True),
    )


class King(Piece):

    char = ["♔", "♚", " "]
    movement = Movement().split(
        Movement().walk(Direction.N),
        Movement().walk(Direction.S),
        Movement().walk(Direction.W),
        Movement().walk(Direction.E),
        Movement().walk(Direction.NE),
        Movement().walk(Direction.SE),
        Movement().walk(Direction.NW),
        Movement().walk(Direction.SW),
    )


def board():
    """Standard board"""

    board = Board(Position(8, 8))

    # white pieces
    board.add(
        (Position(0, 0), Rook(Player.white)),
        (Position(1, 0), Knight(Player.white)),
        (Position(2, 0), Bishop(Player.white)),
        (Position(3, 0), King(Player.white)),
        (Position(4, 0), Queen(Player.white)),
        (Position(5, 0), Bishop(Player.white)),
        (Position(6, 0), Knight(Player.white)),
        (Position(7, 0), Rook(Player.white)),
    )

    # black pieces
    board.add(
        (Position(0, 7), Rook(Player.black)),
        (Position(1, 7), Knight(Player.black)),
        (Position(2, 7), Bishop(Player.black)),
        (Position(3, 7), King(Player.black)),
        (Position(4, 7), Queen(Player.black)),
        (Position(5, 7), Bishop(Player.black)),
        (Position(6, 7), Knight(Player.black)),
        (Position(7, 7), Rook(Player.black)),
    )

    # white pawns
    for i in range(8):
        board[i, 1] = Pawn(Player.white)

    # black pawns
    for i in range(8):
        board[i, 6] = Pawn(Player.black)

    return board
