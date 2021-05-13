from typing import List, Optional, Tuple, Union

from .movement import Movement
from .player import Player


class Piece:
    """Piece"""

    char = ["?", "?", "?"]
    movement: Union[Movement, List[Movement]]

    def __init__(
        self,
        owner: Player,
        char: Optional[Tuple[str, str, str]] = None,
        mop: bool = False,
    ):
        self.char = char or self.char
        self.owner = owner
        self.mop = mop
        self.moves_count = 0
