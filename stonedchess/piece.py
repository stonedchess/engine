from typing import Optional

from .movement import Direction, Movement


class Piece:
    """Piece"""

    char = "?"
    movement: Movement

    def __init__(self, char: Optional[str] = None):
        self.char = char or self.char


class Rook(Piece):

    char = ""
    movement = Movement().split(
        Movement().walk(Direction.N, extend=True),
        Movement().walk(Direction.S, extend=True),
        Movement().walk(Direction.W, extend=True),
        Movement().walk(Direction.E, extend=True),
    )


class Bishop(Piece):

    char = ""
    movement = Movement().split(
        Movement().walk(Direction.NE, extend=True),
        Movement().walk(Direction.SE, extend=True),
        Movement().walk(Direction.NW, extend=True),
        Movement().walk(Direction.SW, extend=True),
    )


class Knight(Piece):

    char = ""
    movement = Movement(jumps=True).split(
        Movement()
        .walk(Direction.N, amount=2)
        .split(
            Movement().walk(Direction.E),
            Movement().walk(Direction.W),
        ),
        Movement()
        .walk(Direction.S, amount=2)
        .split(
            Movement().walk(Direction.E),
            Movement().walk(Direction.W),
        ),
        Movement()
        .walk(Direction.W, amount=2)
        .split(
            Movement().walk(Direction.N),
            Movement().walk(Direction.S),
        ),
        Movement()
        .walk(Direction.E, amount=2)
        .split(
            Movement().walk(Direction.N),
            Movement().walk(Direction.S),
        ),
    )


class Pawn(Piece):

    char = ""
    movement = Movement().walk(Direction.N)


class Queen(Piece):

    char = ""
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

    char = ""
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
