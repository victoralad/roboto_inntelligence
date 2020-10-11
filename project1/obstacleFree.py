#!/usr/bin/env python3.6

import math

# Check that the edge connected x_nearest and x_new does not pass through the any of the obstacle regions.
# Return True if collision occurs and return false otherwise.
def CollisionFree(x_nearest, x_new, obstacles):
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
    distances = [[abs(a*obstacle[0] + b*obstacle[1] + c) / math.sqrt(a**2 + b**2), obstacle[2]] for obstacle in obstacles]
    # Check that the distance to each obstacle is greater than the radius of each obstacle.
    # Add a buffer of 1.0 to account for the radius of the robot (1.0 m).
    return all(distance[0] > distance[1] + 1.0 for distance in distances)