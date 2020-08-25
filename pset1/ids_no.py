#!/usr/bin/env python3.6

import time
import adj_dict

def OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost):
    print("Time(s): ", time_t)
    print("# Paths Popped from Queue: ", no_of_paths_popped)
    print("Max Queue Size: ", max_queue_size)
    print("Returned path's cost: ", path_cost)

def GetPathIDS(adj_dict, start, end):
    # Initialize results
    time_t = 0
    no_of_paths_popped = 0
    max_queue_size = 1
    path_cost = 0

    # Check if the start is the goal
    if start == end:
        OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost)

    # Get the start time
    start_time = time.time()

    # Initialize depth.
    depth = 0

    # Keep searching through the graph as long as the queue is not empty.
    while True:
        # Queue to traverse the graph and append the starting point.
        queue_t = [[start]]

        # List to store visited nodes in the graph.
        visited = []

        depth += 1

        # Get the first path in the queue.
        path = queue_t[0]
        while len(path) <= depth:
            max_queue_size = max(max_queue_size, len(queue_t))
            # Remove the first path from the queue
            path = queue_t.pop()
            no_of_paths_popped += 1
            # Get the last node from the path
            node = path[-1]
            neighbors = sorted(adj_dict[node])
            if  node not in visited:
                neighbors = sorted(adj_dict[node])
                # Loop through all the neighbors of the node.
                # Create a new path for each neighbor and add the new path to the end of the queue.
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue_t.append(new_path)
                    if neighbor == end:
                        path_cost = len(new_path) - 1
                        # Get the stoppage time when the path has been found.
                        end_time = time.time()
                        time_t = end_time - start_time
                        OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost)
                        return new_path
                # Mark node as visited.
                visited.append(node)
    return OutputResult('infeasible', 'infeasible', 'infeasible', 'infeasible')
    
if __name__ == "__main__":
    # Get the adjacency list from adj_dict.
    adj_dict = adj_dict.adj_dict

    start = 'WA'
    end = 'GA'

    GetPathIDS(adj_dict, start, end)

# Reference: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/