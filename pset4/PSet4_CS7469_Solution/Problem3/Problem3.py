# CS 4649/7469 - PSet3: Problem 3
# Solution (by E. Seraj - TA)

import matplotlib.pyplot as plt
import matplotlib.patches as mpathes
import numpy as np


##############################################################################################################
# RRT Class ##################################################################################################
class RRT(object):
    
    # get node for RRT #######################################################################################
    class GetNode(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.parent = None
    
    # initi function #########################################################################################
    def __init__(self, env_size=None, start_node=None, goal_node=None, obstacle_coords=None):
        
        # check input arguments
        if env_size is None or start_node is None or goal_node is None or obstacle_coords is None:
            raise ValueError(">> Oops!! Wait, NOT so fast! RRT() needs all its input arguments to proceed!")
        
        # get the environment size
        self.size_x = env_size[0]
        self.size_y = env_size[1]
        
        # get start and end nodes
        self.start = start_node
        self.goal = goal_node
        self.start_node = self.GetNode(start_node[0], start_node[1])
        
        # get the obstacle coordinates
        self.obstacle = obstacle_coords
        
        # simulation parameters        
        self.step = 0.1         # step size
        self.max_iter = 3000    # number of iterations per run
        self.f = 50   # sampling frequency
        
        # some other params
        self.all_nodes = [self.start_node]
        self.final_path = []

    # generate a random node #################################################################################
    def generate_random_node(self):
        node_x, node_y = np.random.uniform(0, self.size_x), np.random.uniform(0, self.size_y)
        node = [node_x, node_y]
        return node

    # planning ###############################################################################################
    def planning(self, rnd_node):
        min_dist_idx = 0
        min_distance = self.size_y * self.size_y + self.size_x * self.size_x
        for i in range(len(self.all_nodes)):
            node = self.all_nodes[i]
            temp1 = (node.y - rnd_node[1]) * (node.y - rnd_node[1])
            temp2 = (node.x - rnd_node[0]) * (node.x - rnd_node[0])
            temp =  temp1 + temp2
            current_distance = temp
            if current_distance < min_distance:
                min_distance = current_distance
                min_dist_idx = i
        return min_dist_idx

    # steer function #########################################################################################
    def steer(self, min_dist_idx, rnd_node):
        node = self.all_nodes[min_dist_idx]
        temp1 = (node.y - self.goal[1]) * (node.y - self.goal[1])
        temp2 = (node.x - self.goal[0]) * (node.x - self.goal[0])
        cond = temp1 + temp2
        if  cond  <= self.step * self.step:
            new_pose = self.GetNode(self.goal[0], self.goal[1])
            at_goal_flg = 1
        else:
            temp11 = (rnd_node[1] - node.y) * (rnd_node[1]- node.y)
            temp22 = (rnd_node[0] - node.x) * (rnd_node[0] - node.x)
            distance = np.sqrt(temp11 + temp22)
            node_x_modified = min(self.size_x, max(0, node.x + (rnd_node[0] - node.x) / distance * self.step))
            node_y_modified = min(self.size_y, max(0, node.y + (rnd_node[1] - node.y) / distance * self.step))
            new_pose = self.GetNode(node_x_modified, node_y_modified)
            at_goal_flg = 0
        return new_pose, at_goal_flg

    # checking obstacle collision ############################################################################
    def obstacle_collision_check(self, node_near, new_pose):
        for i in range(self.f + 1):
            for j in range(self.f + 1):
                coords_x = new_pose.x + (node_near.x - new_pose.x) / self.f * i
                coords_y = new_pose.y + (node_near.y - new_pose.y) / self.f * j
                if coords_x >= self.obstacle[0] and coords_x <= self.obstacle[2] and coords_y >= self.obstacle[1] \
                         and coords_y <= self.obstacle[3]:
                    return False
        return True
    
    # performing RRT steps ###################################################################################
    def do_rrt(self):
        for i in range(self.max_iter):
            rnd_node = self.generate_random_node()
            min_dist_idx = self.planning(rnd_node)
            new_pose, at_goal_flg = self.steer(min_dist_idx, rnd_node)
            if self.obstacle_collision_check(new_pose, self.all_nodes[min_dist_idx]):
                new_pose.parent = self.all_nodes[min_dist_idx]
                self.all_nodes.append(new_pose)
                if at_goal_flg:
                    this_node = self.all_nodes[-1]
                    while this_node.parent:
                        self.final_path = self.final_path + [this_node]
                        this_node = this_node.parent
        
        # plot the map
        plt.figure(num=1, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')
        width, height = self.obstacle[2] - self.obstacle[0], self.obstacle[3] - self.obstacle[1]
        obstacle_shape = mpathes.Rectangle((self.obstacle[0], self.obstacle[1]), width, height, color='k')
        plt.gca().add_patch(obstacle_shape)
        plt.text(3.075, 5, 'CS 4649/7469 - PSet#4 Solution (RRT)', color='white', fontsize=12, fontweight='bold')

        # adding start and end positions
        plt.plot(self.start[0], self.start[1], "sm", markersize=20)
        plt.plot(self.goal[0], self.goal[1], "sg", markersize=20)

        # plotting the map (tree)
        for node in self.all_nodes:
            if node.parent is not None:
                plt.plot([node.x, node.parent.x], [node.y, node.parent.y], "-b", linewidth=2)
                plt.plot(node.x, node.y, ".r")

        # plotting the final path found
        for node in self.final_path:
            if node.parent is not None:
                plt.plot([node.x, node.parent.x], [node.y, node.parent.y], "-k", linewidth=2)
        plt.axis([0, self.size_x, 0, self.size_y])
        plt.title('RRT Map and Final Planned Path')
        plt.ylabel('Y')
        plt.xlabel('X')


##############################################################################################################
# Main #######################################################################################################
if __name__ == '__main__':
    boundaries = [10, 10]                  # for environment size
    Start = [1, 1]                         # starting position
    Goal = [9, 9]                          # goal position
    Obstacle_coordinates = [3, 3, 7, 7]    # bottom-left and top-right coordinates of the rectangular obstacle
    
    # run RRT
    env_init = RRT(env_size=boundaries, start_node=Start, goal_node=Goal, obstacle_coords=Obstacle_coordinates)
    env_init.do_rrt()  # perform RRT

plt.show()

