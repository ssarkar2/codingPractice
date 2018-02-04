#!/bin/python
#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
import sys

def catAndMouse(x, y, z):
    if abs(x-z) > abs(y-z):
        return 'Cat B'
    elif abs(x-z) < abs(y-z):
        return 'Cat A'
    else:
        return 'Mouse C'

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print result
        #print " ".join(map(str, result))



