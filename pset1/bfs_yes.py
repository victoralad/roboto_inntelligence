#!/usr/bin/env python3.6

import adj_dict

# Get the adjacency list from adj_dict.
adj_dict = adj_dict.adj_dict

# Create a queue to traverse the graph and append the starting point.
queue_t = []
queue_t.append('WA')

# Create list to store visited nodes in the graph.
visited_list = []
visited_list.append('WA')

# Placeholder to determine if goal has been reached.
goal_reached = False

while (visited_list and goal_reached is False):
    print(adj_dict[queue_t[0]])
    for child in adj_dict[queue_t[0]]:
        if child not in visited_list:
            queue_t.append(child)
            visited_list.append(child)
        if child is 'GA':
            goal_reached = True
            break
    queue_t.pop(0)