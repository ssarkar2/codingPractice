#!/bin/python
#https://www.hackerrank.com/challenges/camelcase/problem
import sys

def camelcase(s):
    sm = 0
    for ch in s:
        if ch.upper() == ch:
            sm+= 1
    return sm+1

if __name__ == "__main__":
    s = raw_input().strip()
    result = camelcase(s)
    print result
