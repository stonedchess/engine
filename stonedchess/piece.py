from typing import Dict, List, Optional, Tuple, Union

from .movement import Movement
from .player import Player


class Piece:
    """Piece"""

    char = ["?", "?", "?"]
    movement: Union[Movement, List[Movement]]
    capture: Optional[Movement] = None

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

    @classmethod
    def as_dict(cls) -> Dict:
        """Serialize as dict"""

        movement = cls.movement
        movements = movement if isinstance(movement, list) else [movement]
        capture = cls.capture or Movement()

        return dict(
            char=cls.char,
            movement=[movement.as_dict() for movement in movements],
            capture=capture.as_dict(),
        )

    @staticmethod
    def from_dict(origin: Dict):
        """Serialize from dict"""

        class _Piece(Piece):
            """Deserialized piece"""

            char = origin["char"]
            movement = [Movement.from_dict(mov) for mov in origin["movement"]]
            capture = Movement.from_dict(origin["capture"])

        return _Piece
