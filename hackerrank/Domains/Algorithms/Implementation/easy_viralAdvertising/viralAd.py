#!/bin/python
#https://www.hackerrank.com/challenges/strange-advertising/problem
import sys

def viralAdvertising(n):
    # Complete this 
    if n==1:
        return 2
    tot = 2
    prevday = 2
    for i in range(2,n+1):
        newpeople = prevday*3
        prevday = newpeople/2
        tot += prevday
    return tot

if __name__ == "__main__":
    n = int(raw_input().strip())
    result = viralAdvertising(n)
    print result
