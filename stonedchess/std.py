from typing import Optional

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

    movement = [
        Movement(capture=False).walk(Direction.N, repeat=2),
        Movement(capture=False).walk(Direction.N),
    ]

    capture = Movement().split(
        Movement().walk(Direction.NW),
        Movement().walk(Direction.NE),
    )


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


def fen(fen: Optional[str] = None) -> Board:
    """Parse fen string"""

    pieces_map = dict(
        r=lambda: Rook(Player.black),
        n=lambda: Knight(Player.black),
        b=lambda: Bishop(Player.black),
        q=lambda: Queen(Player.black),
        k=lambda: King(Player.black, mop=True),
        p=lambda: Pawn(Player.black),
        R=lambda: Rook(Player.white),
        N=lambda: Knight(Player.white),
        B=lambda: Bishop(Player.white),
        Q=lambda: Queen(Player.white),
        K=lambda: King(Player.white, mop=True),
        P=lambda: Pawn(Player.white),
    )

    board = Board(Position(8, 8))

    fen = fen or "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1"
    pieces, *_ = fen.split(" ")

    rank = 7
    file = 0

    for char in pieces:

        if char == "/":
            rank -= 1
            file = 0
        elif char.isdigit():
            file += int(char)
        else:
            board[file, rank] = pieces_map[char]()
            file += 1

    return board
