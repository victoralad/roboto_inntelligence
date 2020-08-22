#!/usr/bin/env python3.6

import adj_dict

# Get the adjacency list from adj_dict.
adj_dict = adj_dict.adj_dict

# Queue to traverse the graph and append the starting point.
queue_t = []
queue_t.append(['WA'])

# List to store visited nodes in the graph.
visited_list = []

# List to store path from origin to destination.
path_to_goal = []

# Placeholder to determine if goal has been reached.
goal_reached = False

# Keep searching through the graph as long as the visited list is not empty and the goal has not been reached.
while (queue_t and goal_reached is False):
    # print(queue_t[0], end = " ")
    # print(adj_dict[queue_t[0]])

    # Check if the head of the first path in the queue is the goal.
    if queue_t[0][0] is 'GA':
        goal_reached = True
        break
    # # Loop through the first node at the head of the queue.
    # for child in adj_dict[queue_t[0]]:
    if  queue_t[0][0] not in visited_list:
        queue_t.append(adj_dict[queue_t[0][0]])
        visited_list.append(queue_t[0][0])

    path_to_goal.append(queue_t[0][0])
    queue_t.pop(0)

    print(queue_t)