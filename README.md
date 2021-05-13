# stonedchess - engine

## Usage

Must be used as a python module.
We recommend git submodules to do such.

### Example usage

``` python
from stonedchess.board import Board
from stonedchess.piece import std
from stonedchess.position import Position
from stonedchess.render import render

board = Board(Position(20, 5)).add(
    (2, 2, std.Knight()),
)

moves = board.moves(Position(2, 2))
print(render(board, moves))

# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |   |.  |   |.  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |.  |   |   |   |.  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |   |   |  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |.  |   |   |   |.  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
# |   |.  |   |.  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
# +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
```

### Make custom pieces

``` python
# Let's make a Knight

from stonedchess.movement import Direction, Movement
from stonedchess.piece import Piece

class Knight(Piece):
    """My really custom knight"""

    # Defining piece movement
    movement = Movement().split(
        Movement(jumps=True)
        .walk(Direction.N, amount=2)
        .split(
            Movement().walk(Direction.E),
            Movement().walk(Direction.W),
        ),
        Movement(jumps=True)
        .walk(Direction.S, amount=2)
        .split(
            Movement().walk(Direction.E),
            Movement().walk(Direction.W),
        ),
        Movement(jumps=True)
        .walk(Direction.W, amount=2)
        .split(
            Movement().walk(Direction.N),
            Movement().walk(Direction.S),
        ),
        Movement(jumps=True)
        .walk(Direction.E, amount=2)
        .split(
            Movement().walk(Direction.N),
            Movement().walk(Direction.S),
        ),
    )
```

#### Movement directives

``` python
# Walk stright for n cells
Movement().walk(direction: Direction, amount: int, extend: bool)

# Split path
Movement().split(*branches: Movement)
```

## Tests
```sh
python -m unittest discover test -v
```