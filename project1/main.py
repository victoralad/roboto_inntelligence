#!/usr/bin/env python3.6

import display
import operator
import math
import numpy as np

class RRT:
    def __init__(self, start, obstacles):
        self.start = start
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
    
    # Grow the tree from x_nearest towards x_rand.
    # For this homework, just assume x_new = x_rand.
    def Steer(self, x_nearest, x_rand):
        x_new = x_rand
        return x_new
    
    # Check that the edge connected x_nearest and x_new does not pass through the any of the obstacle regions.
    # Return True if collision occurs and return false otherwise.
    def CollisionFree(self, x_nearest, x_new):
        # Shortest distance from the center of a circle to a line is given by the following equation:
        # dist = |a*x0 + b*y0 + c| / sqrt(a^2 + b^2)
        # where the equation of the line is given by: ax + by + c = 0
        # and the center of the circle is located at (x0,y0).
        # Reference: https://www.geeksforgeeks.org/python-math-function-sqrt/
        line_slope = (x_new[1] - x_nearest[1]) / (x_new[0] - x_nearest[0])
        a = -line_slope
        b = 1
        c = line_slope * x_nearest[0] - x_nearest[1]
        # Calculate the shortest distance from the line segment [x_nearest, x_new]
        # to the center of each obstacle (circle) in obstacles.
        distances = [[abs(a*obstacle[0] + b*obstacle[1] + c) / math.sqrt(a**2 + b**2), obstacle[2]] for obstacle in self.obstacles]
        # Check that the distance to each obstacle is greater than the radius of each obstacle.
        # Add a buffer of 1.0 to account for the radius of the robot (1.0 m).
        return all(distance[0] > distance[1] + 1.0 for distance in distances)
    
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
            # print(x_new)
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
    
    Display(start_coord, goal_coord, obstacle_coords, vertices, edges)
