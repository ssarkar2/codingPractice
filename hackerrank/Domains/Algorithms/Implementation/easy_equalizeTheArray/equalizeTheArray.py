#!/bin/python
#https://www.hackerrank.com/challenges/equality-in-a-array/problem
import sys

def equalizeArray(arr):
    d = {}
    for k in arr:
        d[k] = d.get(k,0)+1
    mx = max(d.values())
    return len(arr) - mx

    
            

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = equalizeArray(arr)
    print result
