from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Position:
    """Vector-like position"""

    file: int
    rank: int

    def __add__(self, other):
        """Vector-like add"""

        file = self.file + other.file
        rank = self.rank + other.rank
        return Position(file, rank)
