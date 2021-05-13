from enum import Enum


class Player(Enum):
    """Players"""

    white = 0
    black = 1
    neutral = 2

    @property
    def opponent(self):
        """Get opponent"""

        if self == Player.black:
            return Player.white
        elif self == Player.white:
            return Player.black

        return Player.neutral
