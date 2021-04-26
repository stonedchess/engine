from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from .position import Position


class Direction(Enum):
    """Movement directions"""

    none = Position(0, 0)
    right = Position(1, 0)
    left = Position(-1, 0)
    top = Position(0, 1)
    bottom = Position(0, -1)
    right_top = Position(1, 1)
    right_bottom = Position(1, -1)
    left_top = Position(-1, 1)
    left_bottom = Position(-1, -1)


class Movement:
    """Piece movement"""

    @dataclass
    class Node:
        """Movement graph node"""

        direction: Direction
        amount: int
        branches: List

        jumps: bool = False

    def __init__(self, jumps: bool = False):
        self.jumps = jumps
        self.graph = self.Node(Direction.none, 0, [], jumps)

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
        jumps: Optional[bool] = None,
    ):
        """Walk a direction"""

        jumps = jumps if jumps is not None else self.jumps

        for leaf in self.leafs():
            node = self.Node(direction, amount, [], jumps)
            leaf.branches.append(node)

        return self

    def split(self, *branches):
        """Split the path in different branches"""

        for leaf in self.leafs():
            for graph in branches:

                graph = graph if isinstance(graph, self.Node) else graph.graph
                leaf.branches += graph.branches

        return self
