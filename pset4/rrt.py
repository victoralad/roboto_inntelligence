#!/usr/bin/env python3.6

import numpy as np

class Node:
    def __init__(self, location):
        assert location is not None
        self.location = location
        self.next_node = None
        # print(self.location)

class RRT:
    def __init__(self, start):
        self.start = Node(start)
        self.vertices = np.array([self.start])
        self.edges = np.array([])
        # print(self.vertices[0].location)

    # Find the nearest node on the tree to x_rand.
    def Nearest(self, x_rand):
        x_nearest = (1, 1)
        return x_nearest
    
    # Grow the tree from x_nearest towards x_rand.
    # For this homework, just assume x_new = x_rand.
    def Steer(self, x_nearest, x_rand):
        x_new = x_rand
        return x_new
    
    # Check if x_new is located outside the obstacle region.
    # Also check that the edge connected x_nearest and x_new
    # does not pass through the obstacle region.
    def ObstacleFree(self, x_nearest, x_new):
        return True

def getTree(num_iterations):
    start = (1, 1)
    goal = (9, 9)
    rrt = RRT(start)

    for i in range(num_iterations):
        # To generate a 2D point between points A = (0, 0) and B = (10, 10)
        # use the formula A + (B - A)*rand(2)
        x_rand = tuple(10*np.random.rand(2))
        x_nearest = rrt.Nearest(x_rand)
        x_new = rrt.Steer(x_nearest, x_rand)
        if rrt.ObstacleFree(x_nearest, x_new):
            rrt.vertices = np.append(rrt.vertices, x_new)
            rrt.edges = np.append(rrt.edges, [x_nearest, x_new])
    return rrt.vertices, rrt.edges

if __name__ == "__main__":
    vertices, edges = getTree(10)
    print(vertices)