#!/bin/python
#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
import sys

def minimumAbsoluteDifference(n, arr):
    # Complete this function
    tmp = sorted(arr)
    return min([abs(tmp[i-1]-tmp[i]) for i in range(1,len(tmp))])

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = minimumAbsoluteDifference(n, arr)
    print result
