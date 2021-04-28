from .movement import Direction, Movement


class Piece:
    """Piece"""

    movement: Movement

    def __init__(self, char: str = "?"):
        self.char = char


class Rook(Piece):

    movement = Movement().split(
        Movement().walk(Direction.N, extend=True),
        Movement().walk(Direction.S, extend=True),
        Movement().walk(Direction.W, extend=True),
        Movement().walk(Direction.E, extend=True),
    )


class Bishop(Piece):

    movement = Movement().split(
        Movement().walk(Direction.NE, extend=True),
        Movement().walk(Direction.SE, extend=True),
        Movement().walk(Direction.NW, extend=True),
        Movement().walk(Direction.SW, extend=True),
    )


class Knight(Piece):

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

    movement = Movement().walk(Direction.N)


class Queen(Piece):

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
