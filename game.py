#!/usr/bin/python3

### CSCI-B 351 / COGS-Q 351 Spring 2022
### Framework code copyright 2022 B351/Q351 instruction team.
### Do not copy or redistribute this code without permission
### and do not share your solutions outside of this class.
### Doing so constitutes academic misconduct and copyright infringement.


import sys
import chess

from board import Board
from baseplayer import *


class Game:
    def __init__(self, trace, player1, player2):
        self._trace = trace
        self.player1 = player1
        self.player2 = player2

    def runGame(self):
        board = Board(self._trace)

        while not board.game_over:
            # finds the move to make
            if board.turn == 0:
                if not isinstance(self.player1, RandomPlayer):
                    print("Player 1 is thinking")

                move = self.player1.findMove(board._trace)
            else:
                if not isinstance(self.player2, RandomPlayer):
                    print("Player 2 is thinking")
                move = self.player2.findMove(board._trace)

            # makes the move
            board.makemove(move)
            board.print()

        # determines if the game is over or not
        if board.winner == 0 and bool(board.is_statlemate()) == True:
            print("It is a draw!")
        elif board.winner == True:
            print("Player 1 wins!")
        elif board.winner == False:
            print("Player 2 wins!")


if __name__ == "__main__":
    # String representing a sequence of moves from a board.
    if len(sys.argv) >= 2:
        trace = sys.argv[1]
    else:
        trace = ""

    # Create player one by calling the
    # player class corresponding to the
    # search algorithm the player uses.
    p1 = RandomPlayer()

    # Same for player 2
    p2 = RandomPlayer()

    # Create the game instance using the
    # board and players you've made.
    g = Game(trace, p1, p2)

    g.runGame()
