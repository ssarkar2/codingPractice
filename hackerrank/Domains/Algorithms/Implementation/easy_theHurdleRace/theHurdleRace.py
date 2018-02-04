#!/bin/python
#https://www.hackerrank.com/challenges/the-hurdle-race/problem
import sys

def hurdleRace(k, height):
    tmp = (max(height)-k)
    return tmp if tmp>0 else 0

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = map(int, raw_input().strip().split(' '))
    result = hurdleRace(k, height)
    print result
