#!/usr/bin/env python3.6

import numpy as np

class Node:
    def __init__(self, location):
        assert location is not None
        self.location = location
        self.next_node = None
        print(self.location)

class RRT:
    def __init__(self):
        start = Node((1, 1))
        

if __name__ == "__main__":
    rrt = RRT()
    # rrt.create_world()