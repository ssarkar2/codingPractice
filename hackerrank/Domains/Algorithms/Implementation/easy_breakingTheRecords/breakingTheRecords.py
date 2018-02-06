#!/bin/python
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
import sys

def breakingRecords(score):
    mn = score[0]; mx = score[0]
    mncnt = 0; mxcnt = 0
    for sc in score:
        if sc > mx:
            mx = sc; mxcnt+=1
        if sc < mn:
            mn = sc; mncnt+=1
    return mxcnt, mncnt

if __name__ == "__main__":
    n = int(raw_input().strip())
    score = map(int, raw_input().strip().split(' '))
    result = breakingRecords(score)
    print " ".join(map(str, result))


