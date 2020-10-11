#!/usr/bin/env python3.6

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


    
def Display(start_coord, goal_coord, obstacle_coords, vertices, edges):

    # -------------------------------------- Create Plots ---------------------------------
    
    plt.figure(num=1, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')

    # Plotting the map (tree).
    # Plot edges.
    for edge in edges:
        plt.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], "-b", linewidth=2)
    # Plot vertices.
    for vertex in vertices:
        plt.plot(vertex[0], vertex[1], ".r")

    # Plot the start and goal locations.
    plt.plot(start_coord[0], start_coord[1], "om", markersize=20)
    plt.plot(goal_coord[0], goal_coord[1], "og", markersize=20)

    # Plot the obstacles.
    for obstacle in obstacle_coords:
        obstacle_shape = mpatches.Circle((obstacle[0], obstacle[1]), obstacle[2], color='k')
        plt.gca().add_patch(obstacle_shape)

    plt.axis([0, 100, 0, 100])
    plt.title('RRT Map and Final Planned Path')
    plt.ylabel('Y')
    plt.xlabel('X')

    plt.savefig("rrt.png")
    plt.show()
