from typing import Callable, List, Optional, Tuple


class Step:
    """Movement step"""

    @staticmethod
    def linear(df: int, dr: int, amount: Optional[int] = None):
        """Linear steps (eg. rook, bishop)"""

        return Step(lambda file, rank: (file + df, rank + dr), amount)

    def __init__(
        self,
        update: Callable[[int, int], Tuple[int, int]],
        amount: Optional[int] = None,
    ):
        self.update = update
        self.amount = amount

    def __call__(self, file: int, rank: int) -> Tuple[int, int]:
        """Update the given position"""

        return self.update(file, rank)


class Movements:
    """Standard movements"""

    rook = [
        Step.linear(0, 1),
        Step.linear(1, 0),
        Step.linear(0, -1),
        Step.linear(-1, 0),
    ]

    bishop = [
        Step.linear(1, 1),
        Step.linear(1, -1),
        Step.linear(-1, 1),
        Step.linear(-1, -1),
    ]

    # TODO create a merge api for the steps
    # an horse move should be made with rook(2) + rook(1)
    horse = [
        Step.linear(2, 1),
        Step.linear(2, -1),
        Step.linear(-2, 1),
        Step.linear(-2, -1),
        Step.linear(1, 2),
        Step.linear(1, -2),
        Step.linear(-1, 2),
        Step.linear(-1, -2),
    ]


class Piece:
    """Piece"""

    movement: List[Step] = Movements.rook
    jumping: bool = False

    def __init__(self, char: str = "?"):
        self.char = char
