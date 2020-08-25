#!/usr/bin/env python3.6

import time

def OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost):
    print("Time(s): ", time_t)
    print("# Paths Popped from Queue: ", no_of_paths_popped)
    print("Max Queue Size: ", max_queue_size)
    print("Returned path's cost: ", path_cost)

def GetPathDFS(adj_dict, start, end):
    # Initialize results
    time_t = 0
    no_of_paths_popped = 0
    max_queue_size = 1
    path_cost = 0

    # Check if the start is the goal
    if start == end:
        OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost)

    # Queue to traverse the graph and append the starting point.
    queue_t = [[start]]

    # Get the start time
    start_time = time.time()

    # Flag to check if a cycle is encountered.
    cycle = False

    # Keep searching through the graph as long as the queue is not empty.
    while queue_t:
        max_queue_size = max(max_queue_size, len(queue_t))
        # Remove the first path from the queue
        path = queue_t.pop()
        no_of_paths_popped += 1
        # Get the last node from the path
        node = path[-1]
        neighbors = sorted(adj_dict[node])
        # Loop through all the neighbors of the node.
        # Create a new path for each neighbor and add the new path to the end of the queue.
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            # Using a heauristic approach to exit the loop when a cycle is detected.
            # There are at most 50 nodes in the graph, so we should not be detecting a path that is longer than 50
            # If we do detect a path longer than 50, then this implies there is a cycle.
            # Note: this does not address a case where the goal is not reachable in the first place. E.g. Hawaii.
            if len(new_path) > 50:
                cycle = True
                break
            queue_t.append(new_path)
            if neighbor == end:
                path_cost = len(new_path) - 1
                # Get the stoppage time when the path has been found.
                end_time = time.time()
                time_t = end_time - start_time
                OutputResult(time_t, no_of_paths_popped, max_queue_size, path_cost)
                print(new_path)
                return new_path
        # Check if cycle has been detected.
        if cycle:
            break
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

    GetPathDFS(adj_dict, start, end)

# Reference: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/