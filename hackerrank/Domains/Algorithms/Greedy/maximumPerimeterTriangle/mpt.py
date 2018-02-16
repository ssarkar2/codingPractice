#!/bin/python
#https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
import sys

def check(a,b,c):
    return (a+b>c) and (b+c>a) and (c+a>b)

def maximumPerimeterTriangle(l):
    # Complete this function
    lst = sorted(l)
    for k in range(len(lst)-1,1,-1):
        #print k
        if lst[k] < lst[k-1]+lst[k-2]:
            return lst[k-2], lst[k-1], lst[k]
    return [-1]
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    l = map(int, raw_input().strip().split(' '))
    result = maximumPerimeterTriangle(l)
    print " ".join(map(str, result))


