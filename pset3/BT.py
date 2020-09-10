#!/usr/bin/env python3.6

import numpy as np
import itertools

def CSP(board_state):
    # Check that row constraint is satisfied.
    # print(board_state)
    if len(set(board_state)) != len(board_state):
        return False
    # Check that diagonal constraint is satisfied.
    output = list(itertools.combinations(enumerate(board_state), 2))
    for i in range(len(output)):
        if output[i][0][1] - output[i][1][1] == output[i][0][0] - output[i][1][0]:
            return False
    return True

def DFS(board_state, domain, variable):

    if CSP(board_state):
        return board_state
    if board_state[variable] >= len(board_state):
        print("hey")
        domain = 1
        variable = 0
        return board_state
    for i in range(len(board_state)):
        # for j in range(len(board_state)):
        board_state[variable] = domain
        print(i, variable, domain, board_state)
        DFS(board_state, domain + 1, variable + i)
            
    return board_state

if __name__ == "__main__":
    N = 4
    board_state = np.ones(N, dtype=int).tolist()
    # domain = np.ones(N, dtype=int).tolist()
    # print(board_state)
    valid_state = DFS(board_state, 1, 0)
    # print(valid_state)

# Reference: Used part of solution code for dfs with visited list, from Pset1.