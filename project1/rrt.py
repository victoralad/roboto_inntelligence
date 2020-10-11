#!/usr/bin/env python3.6

import operator
import numpy as np
import shapely.geometry as sg
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class RRT:
    def __init__(self, start, obstacles):
        self.start = start
        # Create obstacles that are circular using sg.Point(x,y).buffer(radius) and list comprehension in Python.
        self.obstacles = [sg.Point(obstacle[0], obstacle[1]).buffer(obstacle[2]).boundary for obstacle in obstacles]
        # print(self.obstacles[0])
        # temp = [(3, 3), (3, 7), (7, 7), (7, 3)]
        # print(sg.Polygon(temp))
        # temp = sg.Point(1, 2).buffer(2)
        # print(temp)
        # print(list(temp.exterior.coords))

        self.vertices = [self.start]
        self.edges = []

    # Find the nearest node on the tree to x_rand.
    def Nearest(self, x_rand):
        min_dist = float("inf")
        x_nearest = self.vertices[0]
        for vertex in self.vertices:
            if np.linalg.norm(tuple(map(operator.sub, x_rand, vertex))) < min_dist:
                min_dist = np.linalg.norm(tuple(map(operator.sub, x_rand, vertex)))
                x_nearest = vertex
        return x_nearest
    
    # Grow the tree from x_nearest towards x_rand.
    # For this homework, just assume x_new = x_rand.
    def Steer(self, x_nearest, x_rand):
        x_new = x_rand
        return x_new
    
    # Check that the edge connected x_nearest and x_new does not pass through the any of the obstacle regions.
    # Return True if collision occurs and return false otherwise.
    def CollisionFree(self, x_nearest, x_new):
        line = sg.LineString([x_nearest, x_new])
        # # linestrings = list(self.obstacles.exterior.coords)
        # # print(linestrings)
        # for obstacle in self.obstacles:
        #     print(list(obstacle.exterior.coords))
        #     collision = all(line.intersection(sg.LineStringlinestring) for linestring in list(obstacle.exterior.coords))
        #     if collision:
        #         return False
        # return True
        print(self.obstacles[0])
        return not all(line.intersection(sg.LineString(obstacle.exterior.coords)) for obstacle in self.obstacles)
        # if line.intersection(self.obstacles):
        #     return False
        # return True
    
def getTree(num_iterations, start, goal, obstacles):
    world_size = 100 # (0, 0) -> (100, 100)
    start = tuple([start[0], start[1]])
    # print(obstacles)

    rrt = RRT(start, obstacles)

    for i in range(num_iterations):
        # To generate a random 2D point in a plane with corners A = (0, 0) and B = (100, 100)
        # use the formula A + (B - A)*rand(2)
        x_rand = tuple(world_size * np.random.rand(2))
        x_nearest = rrt.Nearest(x_rand)
        x_new = rrt.Steer(x_nearest, x_rand)
        if rrt.CollisionFree(x_nearest, x_new):
            print(x_new)
            rrt.vertices.append(x_new)
            rrt.edges.append([x_nearest, x_new])
            break
    return rrt.vertices, rrt.edges


if __name__ == "__main__":

    # ---------------------------------Get Environment parameters ------------------------

    # Set map coordinates.
    map_coord = [0, 100, 0, 100]

    # Get start coordinates (x, y, theta).
    start_coord = open('start.txt', 'r').read()
    start_coord = tuple(map(float, start_coord.split(',')))

    # Get goal coordinates (x, y).
    goal_coord = open('goal.txt', 'r').read()
    goal_coord = tuple(map(float, goal_coord.split(',')))

    # Get the coordinates of the obstacles.
    obstacle_coords = open('obstacles.txt', 'r').read().split()
    for i in range(len(obstacle_coords)):
        obstacle_coords[i] = tuple(map(float, obstacle_coords[i].split(',')))

    # ----------------------------------------- Run RRT ----------------------------------------
    
    vertices, edges = getTree(100, start_coord, goal_coord, obstacle_coords)

    # -------------------------------------- Create Plots ---------------------------------
    
    plt.figure(num=1, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')

    # plotting the map (tree)
    for edge in edges:
        plt.plot([edge[0][0], edge[1][0]], [edge[0][1], edge[1][1]], "-b", linewidth=2)
        plt.plot(edge[0][0], edge[0][1], ".r")

    # Plot the start and goal locations.
    plt.plot(start_coord[0], start_coord[1], "sm", markersize=20)
    plt.plot(goal_coord[0], goal_coord[1], "sg", markersize=20)

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
