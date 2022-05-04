import numpy as np
from collections import defaultdict


class MCTS:
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state  # board state
        self.parent = parent  # parent of current node, None if root
        self.parent_action = parent_action  # action carried out by parent, None if root
        self.children = []  # all possible actions from current state
        self._numOfVisits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()  # list of all possible actions
        return

    def untried_actions(self):
        self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions

    def win_loss_difference(self):
        wins = self._results[1]
        losses = self._results[-1]
        return wins - losses

    def get_numOfVisits(self):
        return self._numOfVisits

    def expand(self):
        action = self._untried_actions.pop()
        next_state = self.state.move(action)
        child = MCTS(next_state, parent=self, parent_action=action)
        self.children.append(child)
        return child


def is_terminal_node(self):
    self.state.is_game_over()
