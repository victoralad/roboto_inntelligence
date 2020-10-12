#!/usr/bin/env python3.6

import obstacleFree
import steer
import path
import display

import operator
import numpy as np

class RRT:
    def __init__(self, start, obstacles):
        # Get the (x, y) coordinate
        self.start = tuple([start[0], start[1]])
        self.obstacles = obstacles
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
    
def getTree(num_iterations, start, goal, obstacles):
    world_size = 100 # (0, 0) -> (100, 100)

    rrt = RRT(start, obstacles)

    for i in range(num_iterations):
        # To generate a random 2D point in a plane with corners A = (0, 0) and B = (100, 100)
        # use the formula A + (B - A)*rand(2)
        x_rand = tuple(world_size * np.random.rand(2))
        x_nearest = rrt.Nearest(x_rand)
        x_new = steer.Steer(x_nearest, x_rand)
        if obstacleFree.CollisionFree(x_nearest, x_new, obstacles):
            rrt.vertices.append(x_new)
            rrt.edges.append([x_nearest, x_new])
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
    
    display.Display(map_coord, start_coord, goal_coord, obstacle_coords, vertices, edges)
