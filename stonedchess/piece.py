from .movement import Direction, Movement


class Piece:
    """Piece"""

    movement: Movement

    def __init__(self, char: str = "?"):
        self.char = char


class Rook(Piece):

    # movement = Movement().split(
    #     Movement().walk(Direction.top).paths[0],
    #     Movement().walk(Direction.bottom).paths[0],
    #     Movement().walk(Direction.left).paths[0],
    #     Movement().walk(Direction.right).paths[0],
    # )

    movement = Movement().split(
        Movement().split(
            Movement().walk(Direction.top),
            Movement().walk(Direction.bottom),
        ),
        Movement()
        .walk(Direction.right, 2)
        .split(
            Movement().walk(Direction.top),
            Movement().walk(Direction.bottom),
        ),
    )
