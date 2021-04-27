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

    # movement = Movement().split(
    #     Movement().split(
    #         Movement().walk(Direction.N, 2),
    #         Movement().walk(Direction.S, 2),
    #     ),
    #     Movement(jumps=True)
    #     .walk(Direction.E, 2)
    #     .split(
    #         Movement().walk(Direction.N),
    #         Movement().walk(Direction.S),
    #     ),
    # )
