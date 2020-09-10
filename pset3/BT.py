#!/usr/bin/env python3.6

import numpy as np

# Program to solve N Queen Problem using backtracking.
N = 4
  
# ld is an array where its indices indicate row-col+N-1.
# (N-1) is for shifting the difference to store negative indices 
ld = [0] * 2*N
  
""" rd is an array where its indices indicate row+col  
and used to check whether a queen can be placed on  
right diagonal or not"""
rd = [0] * 2*N
  
# Column array where its indices indicates column and  
# used to check whether a queen can be placed in that row or not
cl = [0] * 2*N
  
# A recursive utility function to solve N Queen problem.
def backtrackNQUtil(board, col):  
      
    # Base case: If all queens are placed then return True.
    if (col >= N): 
        return True
          
    # Consider this column and try placing this queen in all rows one by one.
    for i in range(N): 
          
        # Check if the queen can be placed on board[i][col]
        # Check if a queen can be placed on board[row][col]. 
        # We just need to check ld[row-col+n-1] and rd[row+coln]  
        # where ld and rd are for left and right diagonal respectively
        if ((ld[i - col + N - 1] != 1 and 
             rd[i + col] != 1) and cl[i] != 1): 
                   
            """ Place this queen in board[i][col] """
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
              
            """ recur to place rest of the queens """
            if (backtrackNQUtil(board, col + 1)): 
                return True
                  
            # If placing queen in board[i][col] doesn't lead to a solution,  
            # then remove queen from board[i][col].
            board[i][col] = 0 # Bactrack 
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
              
    # If the queen cannot be placed in any row in this colum col then return False.
    return False
      
# This function solves the N Queen problem using Backtracking. 
def backtrack(): 
    board = np.zeros((N, N), dtype=int)
    backtrackNQUtil(board, 0)
    print(board) 
    return True
       
backtrack()