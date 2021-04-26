from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple


@dataclass
class Move:

    origin: Tuple[int, int]
    destination: Tuple[int, int]


class Direction(Enum):
    """Movement directions"""

    none = (0, 0)

    right = (1, 0)
    left = (-1, 0)
    top = (0, 1)
    bottom = (0, -1)

    right_top = (1, 1)
    right_bottom = (1, -1)
    left_top = (-1, 1)
    left_bottom = (-1, -1)


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


def generate(board, file: int, rank: int) -> List[Move]:
    """Generate moves on the baord"""

    moves = []
    piece = board[file, rank]

    if piece is None:
        return moves

    movement: Movement = piece.movement

    def explore(graph: Movement.Node, file: int, rank: int) -> List[Move]:
        """Explore graph for moves"""

        file_o = file
        rank_o = rank
        ok = True

        df, dr = graph.direction.value
        for i in range(graph.amount):

            file += df
            rank += dr

            if board[file, rank] is not None and not graph.jumps:
                ok = False
                break

        if not ok:
            return []

        moves = []

        if len(graph.branches) == 0:
            moves.append(Move((file_o, rank_o), (file, rank)))

        for branch in graph.branches:
            moves += explore(branch, file, rank)

        return moves

    moves = explore(movement.graph, file, rank)
    return moves
