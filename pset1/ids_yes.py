#!/usr/bin/env python3.6

import time

def OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost):
    print("Time(s): ", time_t)
    print("# Paths Popped from Queue: ", no_of_paths_popped)
    print("Max Queue Size: ", max_queue_size)
    print("Returned path's cost: ", path_cost)

def GetPathIDS(adj_dict, start, end):

    def Ids(path2Goal, depth):
        nonlocal no_of_paths_popped, max_queue_size
        no_of_paths_popped += 1

        max_queue_size = max(max_queue_size, len(queue_t))
        queue_t.pop()

        if depth == 0:
            return
        if path2Goal[-1] == end:
            return path2Goal
        if path2Goal[-1] not in visited:
            neighbors = sorted(adj_dict[path2Goal[-1]])
            # Loop through all the neighbors of the node.
            # Create a new path for each neighbor and add the new path to the end of the queue.
            for neighbor in neighbors:
                queue_t.append(path2Goal)
                if neighbor not in path2Goal:
                    new_path = Ids(path2Goal + [neighbor], depth - 1)
                    if new_path:
                        return new_path
            # Mark node as visited.
            visited.append(path2Goal[-1])

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

    # Keep running DFS and changing the depth at each iteration until a solution is found.
    while True:
        # Queue to traverse the graph and append the starting point.
        queue_t = [[start]]

        depth += 1

        visited = []
        
        path2Goal = Ids(queue_t[0], depth)

        if path2Goal:
            path_cost = len(path2Goal) - 1
            # Get the stoppage time when the path has been found.
            end_time = time.time()
            time_t = end_time - start_time
            OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost)
            return path2Goal

    return OutputResult('infeasible', 'infeasible', 'infeasible', 'infeasible')
    
if __name__ == "__main__":

    # Define graph with adjacency list.
    adj_dict = {
        'AL': ('MS', 'TN', 'GA', 'FL'),
        'AZ': ('CA', 'NV', 'UT', 'NM'),
        'AR': ('MO', 'TN', 'MS', 'LA', 'TX', 'OK'),
        'CA': ('OR', 'NV', 'AZ'),
        'CO': ('WY', 'NE', 'KS', 'OK', 'NM', 'UT'),
        'CT': ('NY', 'MA', 'RI'),
        'DE': ('NJ', 'PA', 'MD'),
        'DC': ('MD', 'VA'),
        'FL': ('AL', 'GA'),
        'GA': ('TN', 'NC', 'SC', 'FL', 'AL'),
        'ID': ('WA', 'MT', 'WY', 'UT', 'NV', 'OR'),
        'IL': ('WI', 'IN', 'KY', 'MO', 'IA'),
        'IN': ('MI', 'OH', 'KY', 'IL'),
        'IA': ('MN', 'WI', 'IL', 'MO', 'NE', 'SD'),
        'KS': ('NE', 'MO', 'OK', 'CO'),
        'KY': ('IN', 'OH', 'WV', 'VA', 'TN', 'MO', 'IL'),
        'LA': ('AR', 'MS', 'TX'),
        'ME': ('NH',),
        'MD': ('PA', 'DE', 'DC', 'VA', 'WV'),
        'MA': ('NH', 'RI', 'CT', 'NY', 'VT'),
        'MI': ('OH', 'IN', 'WI'),
        'MN': ('WI', 'IA', 'SD', 'ND'),
        'MS': ('TN', 'AL', 'LA', 'AR'),
        'MO': ('NE', 'IA', 'IL', 'KY', 'TN', 'AR', 'OK', 'KS'),
        'MT': ('ND', 'SD', 'WY', 'ID'),
        'NE': ('SD', 'IA', 'MO', 'KS', 'CO', 'WY'),
        'NV': ('OR', 'ID', 'UT', 'AZ', 'CA'),
        'NH': ('ME', 'MA', 'VT'),
        'NJ': ('NY', 'DE', 'PA'),
        'NM': ('CO', 'OK', 'TX', 'AZ'),
        'NY': ('VT', 'MA', 'CT', 'NJ', 'PA'),
        'NC': ('VA', 'SC', 'GA', 'TN'),
        'ND': ('MN', 'SD', 'MT'),
        'OH': ('PA', 'WV', 'KY', 'IN', 'MI'),
        'OK': ('KS', 'MO', 'AR', 'TX', 'NM', 'CO'),
        'OR': ('WA', 'ID', 'NV', 'CA'),
        'PA': ('NY', 'NJ', 'DE', 'MD', 'WV', 'OH'),
        'RI': ('MA', 'CT'),
        'SC': ('NC', 'GA'),
        'SD': ('ND', 'MN', 'IA', 'NE', 'WY', 'MT'),
        'TN': ('KY', 'VA', 'NC', 'GA', 'AL', 'MS', 'AR', 'MO'),
        'TX': ('NM', 'OK', 'AR', 'LA'),
        'UT': ('ID', 'WY', 'CO', 'AZ', 'NV'),
        'VT': ('NH', 'MA', 'NY'),
        'VA': ('WV', 'MD', 'DC', 'NC', 'TN', 'KY'),
        'WA': ('ID', 'OR'),
        'WV': ('OH', 'PA', 'MD', 'VA', 'KY'),
        'WI': ('MI', 'IL', 'IA', 'MN'),
        'WY': ('MT', 'SD', 'NE', 'CO', 'UT', 'ID')
    }

    start = 'WA'
    end = 'GA'

    GetPathIDS(adj_dict, start, end)
    # Returned path: ['WA', 'ID', 'MT', 'ND', 'MN', 'IA', 'IL', 'IN', 'KY', 'VA', 'NC', 'GA']

# Reference: https://eddmann.com/posts/using-iterative-deepening-depth-first-search-in-python/