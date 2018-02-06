#!/bin/python
#https://www.hackerrank.com/challenges/mars-exploration/problem
import sys

def marsExploration(s):
    d = {0:'S', 1:'O', 2:'S'}
    return sum([1 for i,ch in enumerate(s) if ch is not d[i%3]])
        

if __name__ == "__main__":
    s = raw_input().strip()
    result = marsExploration(s)
    print result
