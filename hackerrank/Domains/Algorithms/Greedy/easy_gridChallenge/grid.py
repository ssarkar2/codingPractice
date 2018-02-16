#!/bin/python
#https://www.hackerrank.com/challenges/grid-challenge/problem
import sys

def gridChallenge(grid):
    # Complete this function
    prevrow = None
    for row in grid:
        tmp = sorted(row)
        if prevrow is not None:
            for i,j in zip(prevrow, tmp):
                if not(i<=j):
                    return 'NO'
        prevrow = tmp
    return 'YES'
        

if __name__ == "__main__":
    t = int(raw_input().strip()) 
    for _ in range(t):
        n = int(raw_input().strip())
        grid = []
        grid_i = 0
        for grid_i in xrange(n):
            grid_t = str(raw_input().strip())
            grid.append(grid_t)
        result = gridChallenge(grid)
        print result
