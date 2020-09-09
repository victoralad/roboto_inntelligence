#!/usr/bin/env python3.6

import numpy as np
from itertools import permutations

n = 4
board = np.zeros(n, n)
for i in range(n):
    board[0][i] = 1

if __name__ == "__main__":

# allPossible = list(permutations(board))