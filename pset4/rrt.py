#!/usr/bin/env python3.6

import operator
import numpy as np
import shapely.geometry as sg
# import networkx as nx
# import matplotlib.pyplot as plt

class RRT:
    def __init__(self, start, obstacle):
        self.start = start
        self.obstacle = sg.Polygon(obstacle)
        self.vertices = [self.start]
        self.edges = []

    # Find the nearest node on the tree to x_rand.
    def Nearest(self, x_rand):
        min_dist = -1.0
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
    
    # Check that the edge connected x_nearest and x_new
    # does not pass through the obstacle region.
    def ObstacleFree(self, x_nearest, x_new):
        line = sg.LineString([(0, 0), (1, 1)])
        return True
    
def getTree(num_iterations):
    # Define properties of the tree.
    start = (1, 1)
    goal = (9, 9)
    obstacle = [(3, 3), (7, 7), (3, 7), (7, 3)]
    world_size = 10 # (0, 0) -> (10, 10)

    rrt = RRT(start, obstacle)

    for i in range(num_iterations):
        # To generate a 2D point between points A = (0, 0) and B = (10, 10)
        # use the formula A + (B - A)*rand(2)
        x_rand = tuple(world_size * np.random.rand(2))
        x_nearest = rrt.Nearest(x_rand)
        x_new = rrt.Steer(x_nearest, x_rand)
        if rrt.ObstacleFree(x_nearest, x_new):
            rrt.vertices.append(x_new)
            rrt.edges.append([x_nearest, x_new])
    return rrt.vertices, rrt.edges

if __name__ == "__main__":
    vertices, edges = getTree(10)
    # G = nx.Graph()
    # G.add_nodes_from(vertices)
    # G.add_edges_from(edges)
    # nx.draw(G)
    # # nx.draw(G, with_labels=True)
    # plt.show()
    