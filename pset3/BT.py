#!/usr/bin/env python3.6

import time
import numpy as np
import matplotlib.pyplot as plt

global timeout, start_time, end_time

# A recursive utility function to solve N Queen problem.
def backtrackNQUtil(board, col, N, ld, rd, cl):
    global timeout, start_time, end_time
    end_time = time.time() 
    if end_time - start_time > 10*60:
        timeout = True
        return False
    
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
                   
            # Place this queen in board[i][col].
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
              
            # Recur to place rest of the queens.
            if (backtrackNQUtil(board, col + 1, N, ld, rd, cl)): 
                return True
                  
            # If placing queen in board[i][col] doesn't lead to a solution,  
            # then remove queen from board[i][col].
            board[i][col] = 0 # Bactrack 
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
              
    # If the queen cannot be placed in any row in this colum col then return False.
    return False
      
# This function solves the N Queen problem using Backtracking. 
def backtrack(N): 
    
    # ld is an array where its indices indicate row-col+N-1.
    # (N-1) is for shifting the difference to store negative indices 
    ld = [0] * 2*N
    
    # rd is an array where its indices indicate row+col  
    # and used to check whether a queen can be placed on right diagonal or not.
    rd = [0] * 2*N
    
    # Column array where its indices indicates column and  
    # used to check whether a queen can be placed in that row or not
    cl = [0] * 2*N
    board = np.zeros((N, N), dtype=int)
    backtrackNQUtil(board, 0, N, ld, rd, cl)
    return True

if __name__ == "__main__":
    N = 4
    timeout = False
    start_time = time.time()
    n_queens = []
    time_t = []
    while(1):
        # Get the start time
        start_time = time.time()
        backtrack(N)
        if timeout:
            break
        print("N-queens:", N, "  Time(s):", time.time() - start_time)
        n_queens.append(N)
        time_t.append(time.time() - start_time)
        N += 1
    # Plot computation time vs number of queens
    plt.plot(n_queens, time_t)
    plt.ylabel('Computation_time (s)')
    plt.xlabel('# of queens')
    plt.show()
        