#!/usr/bin/env python3.6

import numpy as np
import itertools
import copy

def CSP(board_state):
    # Check that row constraint is satisfied.
    if len(set(board_state)) != len(board_state):
        return False
    # Check that diagonal constraint is satisfied.
    output = list(itertools.combinations(enumerate(board_state), 2))
    for i in range(len(output)):
        if output[i][0][1] - output[i][1][1] == output[i][0][0] - output[i][1][0]:
            return False
    return True

def DFS_visited_list(board_state, goal_node, graph):
	"""
	:param board_state: initial state of the board
	:param goal_node: goal location of search
	:param graph: graph searched through (expects a dict)
	:return:
	"""
	queue = []  # initialize q to empty list
	path = [board_state]
	visited_list = [board_state]  # initialize the visited list with start node
	while CSP(board_state) is False:
		children = graph[path[-1]]  # returns a list of neighboring nodes
		for child in reversed(children):
			if child not in visited_list:
				visited_list.append(child)
				queue.append(copy.deepcopy(path) + [child])  # add to queue
		print(queue)
		path = queue.pop()  # get the next path
	return board_state


if __name__ == "__main__":
    n = 4
    board_state = np.ones(n, dtype=int)
    valid_state = DFS(board)
    print(valid_state)

# Reference: Used part of solution code for dfs with visited list, from Pset1.