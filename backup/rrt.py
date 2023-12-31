#!/usr/bin/env python3.6

import operator
import numpy as np
import shapely.geometry as sg
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class RRT:
    def __init__(self, start, obstacle):
        self.start = start
        self.obstacle = sg.Polygon(obstacle)
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
    
    # Check that the edge connected x_nearest and x_new
    # does not pass through the obstacle region.
    def ObstacleFree(self, x_nearest, x_new):
        line = sg.LineString([x_nearest, x_new])
        if line.intersection(self.obstacle):
            return False
        return True
    
def getTree(num_iterations):
    # Define properties of the tree.
    start = (1, 1)
    goal = (9, 9)
    obstacle = [(3, 3), (3, 7), (7, 7), (7, 3)]
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
    vertices, edges = getTree(1000)
    G = nx.Graph()
    color = []
    node_size = []
    for i in range(len(vertices)):
        if i == 0:
            G.add_node(vertices[i], pos=vertices[i])
            color.append('blue')
            node_size.append(100)
        else:
            G.add_node(vertices[i], pos=vertices[i])
            color.append('green')
            node_size.append(10)
    goal = (9, 9)
    G.add_node((9, 9), pos=(9, 9))
    color.append('red')
    node_size.append(100)
    G.add_edges_from(edges)
    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G, pos=pos, node_color=color, node_size=node_size)

    # O = nx.Graph()
    # O.add_node((5, 5), pos=(5, 5))
    # pos=nx.get_node_attributes(O,'pos')
    # nx.draw(O, pos=pos, node_shape='s', node_color='black', node_size=70000)
    obstacle_shape = patches.Rectangle((3, 3), 4, 4, color='k')
    plt.gca().add_patch(obstacle_shape)

    plt.savefig("rrt.png")
    plt.show()
    