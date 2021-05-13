import argparse
from typing import List

from .board import Board, Move
from .game import Game, moves
from .position import Position
from .std import fen


def render(board: Board, moves: List[Move] = [], newline: str = "\n") -> str:
    """Render the board to ascii characters"""

    sep = "+---" * board.size.file + "+"
    origins = {move.origin for move in moves}
    moves = {move.destination: move for move in moves}
    lines = [sep]

    for rank in range(board.size.rank):

        line = []
        for file in range(board.size.file):
            piece = board[file, rank]
            char = piece.char[piece.owner.value] if piece else " "
            move = moves.get(Position(file, rank))
            move = ["x", "."][board[move.destination] is None] if move else " "
            move = "+" if Position(file, rank) in origins else move
            mop = piece.mop if piece else False
            mop = "!" if mop else " "
            line.append(f"{move}{char}{mop}")

        line = "|".join(["", *line, ""])
        lines += [line, sep]

    return newline.join(lines)


parser = argparse.ArgumentParser(description="StonedChess CLI")
parser.add_argument(
    "--fen",
    default="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1",
    help="Forsyth-Edwards Notation initial state",
)

if __name__ == "__main__":

    args = parser.parse_args()
    game = Game(fen(args.fen))

    selected = None
    selected_moves = []

    print(render(game.board))

    while True:

        inp = input("> ")
        cmd, *args = inp.split(" ")

        if cmd == "select":
            selected = Position(int(args[0]), int(args[1]))
            selected_moves = moves(game, selected)
            print(render(game.board, selected_moves))

        if cmd == "move" and selected is not None:
            destination = Position(int(args[0]), int(args[1]))
            move = Move(selected, destination)
            if move in selected_moves:
                game.board.move(move)
            print(render(game.board))

        if cmd == "undo":
            game.board.undo()
            print(render(game.board))

        elif cmd == "exit":
            break
