from dataclasses import asdict, astuple, dataclass
from enum import Enum
from typing import Dict, List, Optional

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
        capture: bool = True

    def __init__(
        self,
        repeat: int = 1,
        jumps: bool = False,
        extend: bool = False,
        capture: bool = True,
    ):
        self.graph = self.Node(
            direction=Direction.none,
            branches=[],
            amount=0,
            repeat=repeat,
            jumps=jumps,
            extend=extend,
            capture=capture,
        )

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
        capture: Optional[bool] = None,
    ):
        """Walk a direction"""

        jumps = jumps if jumps is not None else self.graph.jumps
        capture = capture if capture is not None else self.graph.capture

        for leaf in self.leafs():
            node = self.Node(
                direction=direction,
                branches=[],
                amount=amount,
                repeat=repeat,
                jumps=jumps,
                extend=extend,
                capture=capture,
            )
            leaf.branches.append(node)

        return self

    def split(self, *branches):
        """Split the path in different branches"""

        for leaf in self.leafs():
            for graph in branches:

                graph = graph if isinstance(graph, self.Node) else graph.graph
                leaf.branches += graph.branches

        return self

    def as_dict(self):
        """Serialize movement graph as dict"""

        def fix_direction(node: self.Node):
            """Recursively convert directions into tuples"""

            node["direction"] = astuple(node["direction"].value)
            for branch in node["branches"]:
                fix_direction(branch)

            return node

        return fix_direction(asdict(self.graph))

    @staticmethod
    def from_dict(origin: Dict):
        """Parse dictified graph"""

        def parse_nodes(node: Dict):
            """Recursively parse nodes"""

            return Movement.Node(
                direction=Direction(Position(*node["direction"])),
                branches=[parse_nodes(branch) for branch in node["branches"]],
                amount=node["amount"],
                repeat=node["repeat"],
                jumps=node["jumps"],
                extend=node["extend"],
                capture=node["capture"],
            )

        movement = Movement()
        movement.graph = parse_nodes(origin)
        return movement
