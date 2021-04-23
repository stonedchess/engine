from typing import Optional, Tuple


class Movements:
    """Movements utilities"""

    def __init__(
        self,
        df: int,
        dr: int,
        steps: int = 1,
        jumps: bool = False,
        extend: bool = False,
    ):
        self.df = df
        self.dr = dr
        self.steps = steps
        self.extend = extend
        self.jumps = jumps

        self.moves = {(df, dr, steps, extend)}

    def gen(
        self, df: Optional[int] = None, dr: Optional[int] = None
    ) -> Tuple[int, int, int, bool, bool]:
        """Generate a move"""

        return (
            df or self.df,
            dr or self.dr,
            self.steps,
            self.extend,
            self.jumps,
        )

    def rotate(self):
        """Rotate along four axis of simmetry"""

        self.moves = {
            self.gen(self.df, self.dr),
            self.gen(self.df, -self.dr),
            self.gen(-self.df, self.dr),
            self.gen(-self.df, -self.dr),
            self.gen(self.dr, self.df),
            self.gen(self.dr, -self.df),
            self.gen(-self.dr, self.df),
            self.gen(-self.dr, -self.df),
        }

        return self

    def add(self, other):
        """Add moves from another movement"""

        self.moves.update(other.moves)
        return self


class Piece:
    """Piece"""

    movement: Movements
    jumping: bool = False

    def __init__(self, char: str = "?"):
        self.char = char


class Rook(Piece):

    movement = Movements(2, 0, steps=4, extend=False).rotate()


# class Knight(Piece):

#     movement = Movements.perpendicular(
#         Movements.rotate(1, 0),
#         Movements.rotate(1, 0),
#     )
