from .movement import Direction, Movement


class Piece:
    """Piece"""

    movement: Movement

    def __init__(self, char: str = "?"):
        self.char = char


class Rook(Piece):

    # movement = Movement().split(
    #     Movement().walk(Direction.top),
    #     Movement().walk(Direction.bottom),
    #     Movement().walk(Direction.left),
    #     Movement().walk(Direction.right),
    # )

    movement = Movement().split(
        Movement().split(
            Movement().walk(Direction.top, 2),
            Movement().walk(Direction.bottom, 2),
        ),
        Movement(jumps=True)
        .walk(Direction.right, 2)
        .split(
            Movement().walk(Direction.top),
            Movement().walk(Direction.bottom),
        ),
    )
