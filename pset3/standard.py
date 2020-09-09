#!/usr/bin/env python3.6

import numpy as np
import itertools

def CSP(board_state):
    # Check that row constraint is satisfied.
    if len(set(board_state)) != len(board_state):
        return False
    # Check that diagonal constraint is satisfied.
    output = list(itertools.combinations(enumerate(board_state), 2))
    for i in range(len(output)):
        if board_state[i][0][1] - board_state[i][1][1] == board_state[i][0][0] - board_state[i][1][0]
    return True

if __name__ == "__main__":
    n = 4
    board_state = np.ones(n, dtype=int)
        