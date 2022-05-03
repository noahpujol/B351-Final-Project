#!/usr/bin/python3


### CSCI-B 351 / COGS-Q 351 Spring 2022
### Framework code copyright 2022 B351/Q351 instruction team.
### Do not copy or redistribute this code without permission
### and do not share your solutions outside of this class.
### Doing so constitutes academic misconduct and copyright infri

import random
import chess
import sys


class Board:
    def __init__(self, trace=None):

        self.string_of_board = "."
        self.string_of_p1_side = None
        self.string_of_p2_side = None
        self.player1_color = None
        self.player2_color = None
        self.board_history = []
        self.board = board = chess.Board()
        self._trace = []
        self.game_over = False
        if not (trace is None):
            for c in trace:
                if not self.isValidMove(int(c)):
                    print("Warning: invalid move skipped.")
                    continue
                self.makeMove(int(c))

    @property
    def p1_color_set(self):
        colored_player1_pieces = list[1, 2, 3, 4, 5, 6]
        for i in colored_player1_pieces:
            self.player1_color = chess.BaseBoard.pieces(self.board, i, 0)
            return hex(self.player1_color)

    @property
    def p2_color_set(self):
        colored_player2_pieces = list[1, 2, 3, 4, 5, 6]
        for i in colored_player2_pieces:
            self.player2_color = chess.BaseBoard.pieces(self.board, i, 1)
            return hex(self.player2_color)

    @property
    def p1_pieces(self):
        self.string_of_board = str(self.board)
        for i in enumerate(self.string_of_board[0:15]):
            if "." in str(self.string_of_board) + (str(self.board)):
                # self.string_of_board(".")
                self.string_of_board = self.string_of_p1_side
        return sys.getsizeof(self.string_of_p1_side) / 4

    @property
    def p2_pieces(self):
        self.string_of_board = str(self.board)
        for i in enumerate(self.string_of_board[15:25]):
            if "." in str(self.string_of_board) + (str(self.board)):
                # self.string_of_board.remove(".")

                self.string_of_board = self.string_of_p2_side
        return sys.getsizeof(self.string_of_p2_side) / 4

    @property
    def turn(self):
        p1color = self.player1_color
        # p2color = self.player2_color
        # if p1color == hex(FFFFFF):
        #     return 0
        # else:
        #     return 1
        return p1color

    @property
    def winner(self):
        if not self.game_over:
            return None
        if self.p1_pieces > self.p2_pieces:
            return self.board.outcome()
        if self.p2_pieces > self.p1_pieces:
            return not (self.board.outcome())
        if self.p2_pieces == self.p1_pieces:
            return self.board.is_stalemate() or self.board.is_insufficient_material()
        return 0

    def isValidMove(self, pieces):
        # to do add cases for pinning, attacking, etc
        if self.p2_pieces == self.p1_pieces:
            return self.board.is_stalemate()
        if self.game_over:
            return self.board.is_check()

        else:
            return self.board.is_insufficient_material()

    def generateVaildMove(self):
        return list(self.board.legal_moves)

    def makemove(self, move):
        self.trace = list(self.board.legal_moves)
        # create new board in stack
        self.board_history = self.board
        player = self.turn

        while self.p1_pieces > 0:
            # move a randompiece forward
            if self.p1_pieces == 16 and player == 0:
                move.from_uci(str(random.choice(self.generatedVaildMoves)))
                if self.isVaildMove(self, self.pieces) == self.board.is_stalemate():
                    print("The game is a Stalemate")
                if self.isVaildMove(self, self.pieces) == self.board.is_check():
                    print("checkmate oof")
                if (
                    self.isVaildMove(self, self.pieces)
                    == self.board.is_insufficient_material()
                ):
                    print("we can't countie the game")
            # else:
            #     Move.from_uci(str(random.choice(self.generatedVaildMoves))
