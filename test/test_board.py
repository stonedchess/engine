import unittest

from stonedchess.board import Board
from stonedchess.piece import Piece


class State(unittest.TestCase):
    """stonedchess.Board states holding tests"""

    def test_index(self):

        board = Board(8, 8)
        self.assertEqual(board.index(0, 0), 0)
        self.assertEqual(board.index(1, 0), 1)
        self.assertEqual(board.index(0, 1), 8)
        self.assertEqual(board.index(7, 7), 63)

    def test_cells(self):

        pieces = [
            (0, 0, Piece()),
            (1, 1, Piece()),
            (3, 7, Piece()),
        ]

        board = Board(8, 8).add(*pieces)
        self.assertEqual(board[0, 0], pieces[0][-1])
        self.assertEqual(board[1, 1], pieces[1][-1])
        self.assertEqual(board[3, 7], pieces[2][-1])
        self.assertIsNone(board[4, 4])

        board[4, 4] = Piece()
        self.assertIsNotNone(board[4, 4])


class Render(unittest.TestCase):
    """stonedchess.Board render tests"""

    def test_1x1(self):

        board = Board(1, 1)
        self.assertEqual(board.render(), "+---+\n|   |\n+---+")

        board[0, 0] = Piece()
        self.assertEqual(board.render(), "+---+\n| ? |\n+---+")

        board[0, 0] = Piece("A")
        self.assertEqual(board.render(), "+---+\n| A |\n+---+")

    def test_render(self):

        board = Board(3, 2).add(
            (2, 0, Piece("@")),
            (1, 0, Piece("*")),
            (0, 1, Piece("^")),
        )

        self.assertEqual(
            board.render(newline=":"),
            ":".join(
                [
                    "+---+---+---+",
                    "|   | * | @ |",
                    "+---+---+---+",
                    "| ^ |   |   |",
                    "+---+---+---+",
                ]
            ),
        )
