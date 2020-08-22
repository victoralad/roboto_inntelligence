#!/usr/bin/env python3.6

import adj_dict

def OutputResult(time, no_of_paths_popped, max_queue_size, path_cost):
    print("Time(s): ", time)
    print("# Paths Popped from Queue: ", no_of_paths_popped)
    print("Max Queue Size: ", max_queue_size)
    print("Returned path's cost: ", path_cost)

def GetPathBFS(adj_dict, start, end):
    # Check if the start is the goal
    if start == end:
        OutputResult(0, 0, 1, 0)

    # Queue to traverse the graph and append the starting point.
    queue_t = [[start]]

    # List to store visited nodes in the graph.
    visited = []

    # List to store path from origin to destination.
    path_to_goal = []

    # Placeholder to determine if goal has been reached.
    goal_reached = False

    # Keep searching through the graph as long as the visited list is not empty and the goal has not been reached.
    while (queue_t and goal_reached is False):

        # Check if the head of the first path in the queue is the goal.
        if queue_t[0][0] == end:
            goal_reached = True
            break
        # # Loop through the first node at the head of the queue.
        # for child in adj_dict[queue_t[0]]:
        if  queue_t[0][0] not in visited:
            queue_t.append(adj_dict[queue_t[0][0]])
            visited.append(queue_t[0][0])

        path_to_goal.append(queue_t[0][0])
        queue_t.pop(0)

        # print(queue_t)

if __name__ == "__main__":
    # Get the adjacency list from adj_dict.
    adj_dict = adj_dict.adj_dict

    start = 'WA'
    end = 'GA'
    GetPathBFS(adj_dict, start, end)

# Reference: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/