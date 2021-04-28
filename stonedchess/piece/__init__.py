from typing import Optional

from ..movement import Movement


class Piece:
    """Piece"""

    char = "?"
    movement: Movement

    def __init__(self, char: Optional[str] = None):
        self.char = char or self.char
