from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from .player import Player
from .position import Position


class Direction(Enum):
    """Movement directions"""

    none = Position(0, 0)
    E = Position(1, 0)
    W = Position(-1, 0)
    N = Position(0, 1)
    S = Position(0, -1)
    NE = Position(1, 1)
    SE = Position(1, -1)
    NW = Position(-1, 1)
    SW = Position(-1, -1)

    def adapt(self, player: Player):
        """Adapt direction to player"""

        if player == Player.black:
            if self == Direction.N:
                return Direction.S
            elif self == Direction.S:
                return Direction.N
            elif self == Direction.NW:
                return Direction.SW
            elif self == Direction.SW:
                return Direction.NW
            elif self == Direction.NE:
                return Direction.SE
            elif self == Direction.SE:
                return Direction.NE

        return self


class Movement:
    """Piece movement"""

    @dataclass
    class Node:
        """Movement graph node"""

        direction: Direction
        branches: List

        amount: int = 1
        repeat: int = 1
        jumps: bool = False
        extend: bool = False

    def __init__(
        self,
        repeat: int = 1,
        jumps: bool = False,
        extend: bool = False,
    ):
        self.graph = self.Node(Direction.none, [], 0, repeat, jumps, extend)

    def leafs(self, graph: Optional[Node] = None) -> List[Node]:
        """Get movement graph leafs"""

        graph = graph or self.graph
        leafs = []

        if len(graph.branches) == 0:
            leafs.append(graph)

        for branch in graph.branches:
            leafs += self.leafs(branch)

        return leafs

    def walk(
        self,
        direction: Direction,
        amount: int = 1,
        repeat: int = 1,
        jumps: Optional[bool] = None,
        extend: bool = False,
    ):
        """Walk a direction"""

        jumps = jumps if jumps is not None else self.graph.jumps

        for leaf in self.leafs():
            node = self.Node(direction, [], amount, repeat, jumps, extend)
            leaf.branches.append(node)

        return self

    def split(self, *branches):
        """Split the path in different branches"""

        for leaf in self.leafs():
            for graph in branches:

                graph = graph if isinstance(graph, self.Node) else graph.graph
                leaf.branches += graph.branches

        return self
