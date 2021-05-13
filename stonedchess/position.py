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

    def __iter__(self):
        """Iterate over every position in a bord of
        position of `self.file` and `self.rank`"""

        for file in range(self.file):
            for rank in range(self.rank):
                yield Position(file, rank)
