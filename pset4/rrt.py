#!/usr/bin/env python3.6

import numpy as np

class RRT:
    def __init__(self):
        
        self.world = self.create_world()
        print(np.flip(self.world, 0))
    def create_world(self):

        world = np.array([])

        for i in range(10):
            world = np.append(world, '0')

        self.world = np.array([world])
        
        for i in range(9):
            self.world = np.vstack([self.world, world])

        # Define goal region.
        self.world[8][8] = 'G'
        # Define start region.
        self.world[1][1] = 'S'

        return self.world

if __name__ == "__main__":
    rrt = RRT()
    rrt.create_world()