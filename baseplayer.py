#!/usr/bin/python3
import math

### CSCI-B 351 / COGS-Q 351 Spring 2022
### Framework code copyright 2022 B351/Q351 instruction team.
### Do not copy or redistribute this code without permission
### and do not share your solutions outside of this class.
### Doing so constitutes academic misconduct and copyright infringement.

import math
import random
from board import Board


class BasePlayer:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    ##################
    #      TODO      #
    ##################
    # Assign integer scores to the three terminal states
    # P2_WIN_SCORE < TIE_SCORE < P1_WIN_SCORE
    # Access these with "self.TIE_SCORE", etc.
    P1_PIECE_VALUE = 29
    P2_PIECE_VALUE = -29
    TIE_SCORE = 0
    # Returns a heuristic for the amount of pieces on the board!
    # for all boards, P2_WIN_SCORE < heuristic(b) < P1_WIN_SCORE
    def heuristic(self, board):
        h1 = 0
        h2 = 0
        for i in board.p1_pieces:  # current pieces player 1 has
            h1 = h1 + 1
        for i in board.p2_pieces:  # current pieces player 2 has
            h2 = h2 + i
        r = float(h1) * 0.5
        r = float(h2) * -0.5
        return r

    """We dont need to implement anything here"""

    def findMove(self, trace):
        raise NotImplementedError


class RandomPlayer(BasePlayer):
    def __init__(self, max_depth=None):
        BasePlayer.__init__(self, max_depth)
        self.random = random.Random(max_depth)

    def findMove(self, trace):
        board = Board(trace)
        options = board.generateVaildMove()
        return self.random.choice(options)


class PlayerMM(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax on board with depth.
    # returns the best move and best score as a tuple
    def minimax(self, board, depth):
        b1 = Board()
        b2 = BasePlayer(depth)
        if terminal == 1:
            return (None, self.P2_WIN_SCORE)
        if terminal == -1:
            return (None, self.TIE_SCORE)
        if depth == 0 and terminal == 0:
            return b2.heuristic(board)
        if b1.turn == 0:
            min_value = -math.inf
            for obj in map(float, b1.p2_pieces):
                makemove(board.legal_moves)
                min_value = min(min_value, self.minimax(board, depth - 1))
                return (min_value, (map(float, b1.p2_pieces[:6])))
        else:
            max_value = math.inf
            for obj in map(float, b1.p1_pieces):
                makemove(board.legal_moves)
                max_value = max(max_value, self.minimax(board, depth - 1))
                return (max_value, (map(float, b1.p1_pieces[:6])))

    def findMove(self, trace):
        board = Board(trace)
        move, score = self.minimax(board, self.max_depth)
        return move
